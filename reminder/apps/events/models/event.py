from django.db import models
from django.utils.translation import gettext_lazy as _lazy

from reminder.apps.core.models import (
    AbstractPublicModel,
    IsActiveModelMixin,
)


class EventStatus(models.TextChoices):

    OPEN = "OPEN", _lazy("Open")
    COMPLETE = "COMPLETE", _lazy("Complete")
    CLOSED = "CLOSED", _lazy("Closed")
    PROCESSING = "PROCESSING", _lazy("Processing")
    NOTIFICATION_FAILED = "NOTIFICATION_FAILED", _lazy("Notification failed")
    PROCESSED = "PROCESSED", _lazy("Processed")


class Event(AbstractPublicModel, IsActiveModelMixin):

    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, default="")
    place = models.CharField(max_length=128)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=32, choices=EventStatus.choices, default=EventStatus.OPEN
    )
