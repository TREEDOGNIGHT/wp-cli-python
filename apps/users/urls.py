from django.urls import path

from apps.users.views import users, add_users

urlpatterns = [
    path('', users, name='users'),
    path('add_users/', add_users, name='add_users')
]
