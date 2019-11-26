from django.urls import path

from apps.users.views import users, groups

urlpatterns = [
    path('users/', users, name='users'),
    path('gp/', groups, name='groups'),
]
