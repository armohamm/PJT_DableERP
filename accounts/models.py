from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 'auth.User'
    title = models.CharField(max_length=20, blank=True)
    team = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    addr = models.CharField(max_length=50, blank=True)
    joindate = models.DateTimeField(max_length=20, blank=True)