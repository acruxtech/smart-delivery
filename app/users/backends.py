from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db import models


User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                models.Q(username__iexact=username) |
                models.Q(email__iexact=username)
            )
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
