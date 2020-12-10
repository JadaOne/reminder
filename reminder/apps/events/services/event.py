from reminder.apps.core.services import update_object
from reminder.apps.users.services import collect_and_check_users

from ..exceptions import (
    EventIsNotActiveException,
    ParticipantAlreadyRegisteredException,
    PermissionDeniedException,
)
from ..models import Event, EventStatus, Participant, UserRole


def create_event(user, **kwargs):

    event = Event.objects.create(**kwargs)
    Participant.objects.create(event=event, user=user, role=UserRole.CREATOR)
    return event


def complete_event(event, user):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    if event.status not in [EventStatus.OPEN, EventStatus.PROCESSED]:
        raise EventIsNotActiveException

    event.status = EventStatus.COMPLETE
    event.save()
    return event


def update_event(event, user, **kwargs):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    if event.status not in [EventStatus.OPEN, EventStatus.PROCESSED]:
        raise EventIsNotActiveException

    return update_object(event, **kwargs)


def add_participants(event, users_list):

    if event.status not in [EventStatus.OPEN, EventStatus.PROCESSED]:
        raise EventIsNotActiveException

    if Participant.objects.filter(
        event=event, user_id__in=[user.id for user in users_list]
    ):
        raise ParticipantAlreadyRegisteredException

    Participant.objects.bulk_create(
        [
            Participant(event=event, user=participant, role=UserRole.INVITEE)
            for participant in users_list
        ]
    )


def process_participants_adding(user, event, email_list):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    users = collect_and_check_users(email_list=email_list)
    add_participants(event=event, users_list=users)
