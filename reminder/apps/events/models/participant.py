from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _lazy

from reminder.apps.core.models import AbstractPrivateModel


class UserRole(models.TextChoices):

    CREATOR = "CREATOR", _lazy("Creator")
    INVITEE = "INVITEE", _lazy("Invitee")


class Participant(AbstractPrivateModel):

    role = models.CharField(max_length=32, choices=UserRole.choices)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="participations",
    )
    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="participants"
    )

    class Meta:
        unique_together = (("user", "event"),)
