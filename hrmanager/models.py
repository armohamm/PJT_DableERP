import os
import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.conf import settings

class Leave(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    leavestart = models.DateTimeField(max_length=100)
    leaveend = models.DateTimeField(max_length=100)
    leaveuses = models.DecimalField()
    reason = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
