from ..exceptions import (
    CreatorCanNotBeRemovedException,
    EventIsNotOpenedException,
    PermissionDeniedException,
)
from ..models import EventStatus, UserRole


def process_participant_deletion(event, participant, user):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    if event.status != EventStatus.OPEN:
        raise EventIsNotOpenedException

    if participant.role == UserRole.CREATOR:
        raise CreatorCanNotBeRemovedException

    participant.delete()
