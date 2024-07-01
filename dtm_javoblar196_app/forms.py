# forms.py
from django import forms

class UserIdForm(forms.Form):
    user_id = forms.CharField(label='ID', max_length=20)
