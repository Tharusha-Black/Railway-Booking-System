from django.contrib.auth.models import AbstractUser
from django.db import models

class RailwayUser(AbstractUser):
    NIC = models.CharField(max_length=12)
    registered_date = models.DateField()
    country = models.CharField(max_length=100)  # Change the max_length as needed
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    # Specify unique related_name attributes for the fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='railwayuser_set',  # Unique related_name for groups
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='railwayuser_set',  # Unique related_name for user_permissions
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )
    
    def __str__(self):
        return self.username
