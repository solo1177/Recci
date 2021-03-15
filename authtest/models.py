from django.db import models


class NewUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
