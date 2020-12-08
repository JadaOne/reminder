from django.db import models
from django.utils.translation import gettext_lazy as _lazy

from uuid import uuid4


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class AbstractPrivateModel(AbstractBaseModel):
    class Meta:
        abstract = True


class AbstractPublicModel(AbstractBaseModel):
    pub_id = models.UUIDField(default=uuid4, editable=False, unique=True, db_index=True)

    class Meta:
        abstract = True


class IsActiveModelMixin(models.Model):

    is_active = models.BooleanField(
        _lazy("active"),
        default=True,
        db_index=True,
        help_text=_lazy(
            "If checked, this object is active. Uncheck to soft delete this object but not any child "
            "or related objects."
        ),
    )

    class Meta:
        abstract = True
