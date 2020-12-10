from ..models import Event, EventStatus
from django_rq import job
from django.core.mail import send_mail
from django.conf import settings
from logging import getLogger
from django.utils.timezone import now


logger = getLogger("default")


@job("default", timeout=60)
def process_item(event_id):

    event = Event.objects.get(id=event_id)

    try:
        send_mail(
            subject=event.title,
            message=event.description,
            from_email=settings.FROM_MAIL,
            recipient_list=list(
                event.participants.values_list("user__email", flat=True)
            ),
        )
        event.status = EventStatus.PROCESSED
        event.save()
    except Exception as e:
        logger.exception(e)
        event.status = EventStatus.NOTIFICATION_FAILED
        event.save()


def process_events():

    events_ids = Event.objects.filter(
        date__lte=now(), status=EventStatus.OPEN
    ).values_list("id", flat=True)
    Event.objects.filter(id__in=events_ids).update(status=EventStatus.PROCESSING)
    for event in events_ids:
        process_events.delay(event)
