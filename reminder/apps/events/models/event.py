from reminder.apps.core.models import AbstractPublicModel, IsActiveModelMixin, AbstractPrivateModel
from django.db import models
from django.utils.translation import gettext_lazy as _lazy
from django.conf import settings


class EventStatus(models.TextChoices):

    OPEN = "OPEN", _lazy("Open")
    COMPLETE = "COMPLETE", _lazy("Complete")
    CLOSED = "CLOSED", _lazy("Closed")


class Event(AbstractPublicModel, IsActiveModelMixin):

    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, default="")
    place = models.CharField(max_length=128)
    date = models.DateTimeField()
    status = models.CharField(max_length=32, choices=EventStatus.choices, default=EventStatus.OPEN)
