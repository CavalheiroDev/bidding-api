from typing import Optional

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, *args, username: str, email: Optional[str] = None, password: Optional[str] = None):
        user = self.model(username=username, email=email, *args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, *args, username: str, email: Optional[str] = None, password: Optional[str] = None):
        user = self.create_user(*args, username=username, email=email, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
