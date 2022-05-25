import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from bidding.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(db_column='ID', unique=True, editable=False, primary_key=True, default=uuid.uuid4())
    username = models.CharField(db_column='USERNAME', max_length=40, unique=True)
    email = models.EmailField(db_column='EMAIL', max_length=255, unique=True, null=True)
    first_name = models.CharField(db_column='FIRST_NAME', max_length=60, null=True)
    last_name = models.CharField(db_column='LAST_NAME', max_length=60, null=True)
    is_active = models.BooleanField(db_column='IS_ACTIVE', default=True)
    is_email_verified = models.BooleanField(db_column='IS_EMAIL_VERIFIED', default=False)
    is_superuser = models.BooleanField(db_column='IS_SUPERUSER', default=False)

    created = models.DateTimeField(db_column='CREATED', auto_now_add=True)
    modified = models.DateTimeField(db_column='MODIFIED', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'USER'
