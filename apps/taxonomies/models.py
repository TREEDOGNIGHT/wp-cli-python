from django.db import models

from apps.commands.models import Command


class Tax(models.Model):
    tax_name = models.CharField(max_length=50)
    tax_type = models.CharField(max_length=10)
    tax_exerpt = models.CharField

class TaxCommand(models.Model):
    Command = models.ForeignKey(
        Command, on_delete=models.CASCADE
    )
    Tax = models.ForeignKey(
        Tax, on_delete=models.CASCADE
    )
    note = models.TextField()
