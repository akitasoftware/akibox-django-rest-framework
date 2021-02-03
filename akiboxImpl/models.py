import uuid
from django.db import models


class User(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid1(), primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=128)

    class Meta:
        ordering = ['last_name']


class File(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid1(), primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()

    class Meta:
        ordering = ['created_at']

