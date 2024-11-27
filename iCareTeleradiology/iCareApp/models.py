from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    # Add related_name to avoid clash with default User model
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Change this related_name
        blank=True
    )
