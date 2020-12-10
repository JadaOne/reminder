from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _lazy
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from reminder.apps.core.utils import validate_UUID
from reminder.apps.events.exceptions import (
    CreatorCanNotBeRemovedException,
    EventIsNotActiveException,
    ParticipantAlreadyRegisteredException,
    PermissionDeniedException,
)
from reminder.apps.events.models import Event, Participant
from reminder.apps.events.services import (
    complete_event,
    create_event,
    process_participant_deletion,
    process_participants_adding,
    update_event,
)

from ..serializers import CreateParticipantSchema, EventSchema
from .filters import EventFilterBackend


class EventView(GenericViewSet, generics.RetrieveAPIView, generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = EventSchema
    filter_backends = [EventFilterBackend]
    lookup_field = "pub_id"
    lookup_url_kwarg = "event_pub_id"

    def get_queryset(self):
        return Event.objects.filter(participants__user=self.request.user)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event = create_event(request.user, **serializer.validated_data)
        return Response(self.get_serializer(event).data, status=status.HTTP_201_CREATED)

    def complete_event(self, request, event_pub_id, *args, **kwargs):

        event = self.get_object()
        try:
            event = complete_event(event, request.user)
        except EventIsNotActiveException:
            raise APIException(
                _lazy("You can not cancel already complete or closed event")
            )
        except PermissionDeniedException:
            raise APIException(
                _lazy("You have to be a creator of the event to cancel it")
            )
        return Response(self.get_serializer(event).data, status=status.HTTP_200_OK)

    def update(self, request, event_pub_id, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = self.get_object()
        try:
            event = update_event(event, request.user, **serializer.validated_data)
        except PermissionDeniedException:
            raise APIException(_lazy("You have to be a creator to update the event"))
        except EventIsNotActiveException:
            raise APIException(
                _lazy("You can not update already canceled or closed event")
            )
        return Response(self.get_serializer(event).data, status=status.HTTP_200_OK)

    def add_participants(self, request, event_pub_id, *args, **kwargs):

        serializer = CreateParticipantSchema(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = self.get_object()
        try:
            process_participants_adding(
                user=request.user, event=event, email_list=serializer.data["emails"]
            )
        except PermissionDeniedException:
            raise APIException(
                _lazy("You have to be a creator to add new participants to the event")
            )
        except EventIsNotActiveException:
            raise APIException(
                _lazy(
                    "You can not add participants to the already canceled or closed event"
                )
            )
        except ParticipantAlreadyRegisteredException:
            raise APIException(_lazy("User can not be added twice to the event"))
        event.refresh_from_db()
        return Response(self.get_serializer(event).data, status=status.HTTP_201_CREATED)

    def delete_participant(self, request, event_pub_id, user_pub_id, *args, **kwargs):

        try:
            validate_UUID(user_pub_id)
        except ValidationError:
            raise APIException(_lazy("Provided pub id is invalid"))
        event = self.get_object()
        participant = get_object_or_404(
            Participant, user__pub_id=user_pub_id, event=event
        )
        try:
            process_participant_deletion(event, participant, user=request.user)
        except PermissionDeniedException:
            raise APIException(
                _lazy("You have to be a creator to remove participants from the event")
            )
        except EventIsNotActiveException:
            raise APIException(
                _lazy(
                    "You can not remove participants from the already complete or closed event"
                )
            )
        except CreatorCanNotBeRemovedException:
            raise APIException(_lazy("Creator can not be deleted from the event"))
        event.refresh_from_db()
        return Response(self.get_serializer(event).data, status=status.HTTP_200_OK)
