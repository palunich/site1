from django.db import models


class User(models.Model):
    email = models.TextField()
    passw = models.TextField()
    money = models.IntegerField(default=0)
