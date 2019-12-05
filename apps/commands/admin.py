from django.contrib import admin

from apps.commands.models import Command, CommandUser

admin.site.register(Command)
admin.site.register(CommandUser)
