import logging

from django.db import transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from rest_framework.exceptions import APIException
from reminder.apps.users.exceptions import UserWithProvidedEmailAlreadyExistsException
from django.utils.translation import gettext_lazy as _lazy
from rest_framework.authtoken.models import Token

from ..serializers import UserSchema
from reminder.apps.users.services import register_user


logger = logging.getLogger(__name__)


class UserRegisterView(CreateAPIView):

    serializer_class = UserSchema
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            user = register_user(**data)
        except UserWithProvidedEmailAlreadyExistsException:
            raise APIException(_lazy("Email is already used."))
        token = Token.objects.create(user=user)
        return Response(
            data={"token": token.key, "user": UserSchema(user).data}, status=status.HTTP_201_CREATED
        )
