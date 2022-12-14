from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"

    phone = models.TextField(max_length=500, blank=True)
    address = models.TextField(max_length=500, blank=True)
