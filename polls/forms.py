from django import forms
from django.db import models


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)

    
