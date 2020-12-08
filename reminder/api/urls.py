from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("users/", include("reminder.api.users.urls")),
    path("auth/token/", obtain_auth_token, name="auth_token"),
    path("events/", include("reminder.api.events.urls")),
]
