import json
import os

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\key.json'
with open(path) as f:
    data = json.load(f)
    secret_key = data["key"]


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='Enter your secret key')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if answer != secret_key:
            raise forms.ValidationError('Wrong')
        return answer