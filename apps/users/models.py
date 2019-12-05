from django.db import models
from django import forms

class User(models.Model):
    user_login = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    user_display_name = models.CharField(max_length=20)
    modified_date = models.DateTimeField(auto_now=True)
    user_email = models.CharField(max_length=50)
    user_status = models.CharField(max_length=50)

class Options(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    op_name = models.CharField(max_length=50)
    op_value = models.CharField(max_length=50)
    op_name = models.CharField(max_length=20)

   
