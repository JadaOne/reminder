from ..exceptions import (
    CreatorCanNotBeRemovedException,
    EventIsNotActiveException,
    PermissionDeniedException,
)
from ..models import EventStatus, UserRole


def process_participant_deletion(event, participant, user):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    if event.status not in [EventStatus.OPEN, EventStatus.PROCESSED]:
        raise EventIsNotActiveException

    if participant.role == UserRole.CREATOR:
        raise CreatorCanNotBeRemovedException

    participant.delete()
