from reminder.apps.core.models import AbstractPublicModel, IsActiveModelMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _lazy
from django.utils import timezone
from ..utils import validate_email
from django.contrib.auth.models import UserManager


class User(AbstractPublicModel, IsActiveModelMixin, AbstractBaseUser):

    username = None
    date_joined = models.DateTimeField(_lazy("Date joined"), default=timezone.now)
    email = models.EmailField(
        _lazy("Email address"), db_index=True, unique=True, validators=[validate_email]
    )
    first_name = models.CharField(max_length=32, blank=False, db_index=True)
    last_name = models.CharField(max_length=32, blank=False, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f"<User id={self.id}, is_active={self.is_active}>"
