from ..models import UserRole, EventStatus
from ..exceptions import PermissionDeniedException, EventIsNotOpenedException, CreatorCanNotBeRemovedException


def process_participant_deletion(event, participant, user):

    if user.participations.get(event=event).role != UserRole.CREATOR:
        raise PermissionDeniedException

    if event.status != EventStatus.OPEN:
        raise EventIsNotOpenedException

    if participant.role == UserRole.CREATOR:
        raise CreatorCanNotBeRemovedException

    participant.delete()
