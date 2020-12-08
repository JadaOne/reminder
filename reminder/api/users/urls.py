from django.urls import path

from .views import UserRegisterView, UserView

app_name = "users"


urlpatterns = [
    path("registration/", UserRegisterView.as_view(), name="user_registration"),
    path("me/", UserView.as_view(), name="user_registration"),
]
