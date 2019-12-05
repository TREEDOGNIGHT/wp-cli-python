from django.contrib import admin
from apps.users.models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'modified_date')
#     list_display_links = ('first_name', 'last_name')
#     search_fields = ('first_name', 'last_name')
#     readonly_fields = ('birth_date',)
