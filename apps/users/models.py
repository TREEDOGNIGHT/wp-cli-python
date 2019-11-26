from django.db import models
from django import forms

class Users(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    password        = models.CharField(max_length=32) 
    modified_date   = models.DateTimeField(auto_now=True)
    test            = models.CharField(max_length=8)
