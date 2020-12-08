from .views import EventView
from django.urls import path


app_name = "events"


urlpatterns = [
    path("", EventView.as_view({"get": "list", "post": "create"}), name="event_view"),
    path(
        "<event_pub_id>/",
        EventView.as_view({"get": "retrieve", "post": "complete_event", "patch": "update"}),
        name="event_detailed"
    ),
    path(
        "<event_pub_id>/participants/",
        EventView.as_view({"post": "add_participants"}),
        name="event_participants"
    ),
    path(
        "<event_pub_id>/participants/<user_pub_id>/",
        EventView.as_view({"delete": "delete_participant"}),
        name="delete_participant"
    ),
]
