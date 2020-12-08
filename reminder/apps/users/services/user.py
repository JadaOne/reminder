from ..exceptions import (
    UnregisteredUsersCanNotBeAddedExceptions,
    UserWithProvidedEmailAlreadyExistsException,
)
from ..models import User


def register_user(email, first_name, last_name, password, **kwargs):
    if User.objects.filter(email=email).exists():
        raise UserWithProvidedEmailAlreadyExistsException()
    user = User(email=email, first_name=first_name, last_name=last_name, **kwargs)
    user.set_password(password)
    user.save()
    return user


def collect_users(email_list):

    return User.objects.filter(email__in=email_list)


def check_user_list(email_list, user):

    if len(user) != len(email_list):
        raise UnregisteredUsersCanNotBeAddedExceptions


def collect_and_check_users(email_list):

    users = collect_users(email_list)
    check_user_list(email_list, users)
    return users
