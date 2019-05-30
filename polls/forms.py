from django import forms
from django.db import models


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)

class SmsForm(models.Model):
    name = models.CharField(max_length = 26)
    number = models.IntegerField(max_length=8)

class VCard(models.Model):
    N = models.CharField(max_length = 20)
    FN = models.CharField(max_length= 50)
    EMAIL = models.EmailField(max_length=40)
    TEL = models.IntegerField(max_length=8)
    
