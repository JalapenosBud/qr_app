import qrcode
from django.db import models

import os
import vobject
import pyqrcode
import png

from django.shortcuts import render
from pathlib import Path
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from QRCODE.settings import BASE_DIR

class WeblinkModel(models.Model):
    weblink = models.CharField(max_length = 250, null=True)
    # LAV EN FORM FOR ID SOM I KAN KALDE PÅ!
    increment_id = models.AutoField(primary_key=True)
    #file_path = os.path.join(BASE_DIR, 'media/')

    def create(self, _weblink):
        self.weblink = _weblink
        #generate(_weblink)
        

    def __str__(self):
        return self.weblink

class WifiModel(models.Model):
    wifiName = models.CharField(max_length = 26)
    wifiPass = models.CharField(max_length=28)
    wifiAuth = models.CharField(max_length=8)

    def create(self, _wifiname, _wifipass, _wifiauth):
        self.wifiName = _wifiname
        self.wifiPass = _wifipass
        self.wifiAuth = _wifiauth
        #userInput = f"WIFI:T:{_wifiauth};S:{_wifiname};P:{_wifipass};;"
        #generate(userInput)

    def __str__(self):
        return self.wifiName + ' ' + self.wifiPass + ' ' + self.wifiAuth


class SmsModel(models.Model):
    textmessage = models.CharField(max_length = 26)
    number = models.CharField(max_length=8)

    def create(self, _textmessage, _number):
        self.textmessage = _textmessage
        self.number = _number
        #userInput = F'sms:{_number}:{_textmessage}.'
        #generate(userInput)

    def __str__(self):
        return self.textmessage + ' ' + self.number


def generate(input):
        qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(input)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        #angelo
        img.save("C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\media\\code.png")

        #kasper
        #img.save("C:\\Users\\Jalap\\Skynet\\qr_app\\qr_app\\media\\code.png")

