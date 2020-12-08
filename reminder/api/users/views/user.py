from rest_framework import generics
from ..serializers import UserSchema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from reminder.apps.core.services import update_object


class UserView(APIView):

    serializer_class = UserSchema
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, only=("first_name", "last_name"))
        serializer.is_valid(raise_exception=True)
        user = update_object(request.user, **serializer.validated_data)
        return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)
