from django import forms
from django.forms import ModelForm, Form


from apps.users.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('user_display_name', 'user_login', 'user_status')


class SearchUserForm(Form):
    search = forms.CharField(max_length=50, required=True)

class SearchUserForm(Form):
    search = forms.CharField(max_length=50, required=True)   

class NewUserForm(Form):
    user_login = forms.CharField(max_length=50)
    user_pass = forms.CharField(max_length=50)
    user_display_name = forms.CharField(max_length=20)
    user_email = forms.CharField(max_length=50)
    user_status = forms.ChoiceField(
        choices=(('admin', 'Admin'),
                 ('qa', 'QA'),)
    )