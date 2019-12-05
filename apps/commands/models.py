from django.db import models

from apps.users.models import User


class Command(models.Model):
    com_author = models.CharField(max_length=50)
    com_body = models.CharField(max_length=10)
    com_exerpt = models.CharField
    com_healine = models.CharField(max_length=10)
    com_mod_date = models.DateTimeField(auto_now=True)
    guid = models.CharField(max_length=10)

class CommandUser(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    Command = models.ForeignKey(
        Command, on_delete=models.CASCADE
    )
    note = models.TextField()
