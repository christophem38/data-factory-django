from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey


class Translation(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    result = models.TextField()
