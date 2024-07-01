# models.py
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user_id
