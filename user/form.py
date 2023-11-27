from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserCreation(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password1', 'password2', 'phone')


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()