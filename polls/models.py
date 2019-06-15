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
    increment_id = models.AutoField(primary_key=True)

    def create(self, _weblink):
        self.weblink = _weblink 

    def __str__(self):
        return self.weblink

class WifiModel(models.Model):
    wifiName = models.CharField(max_length = 26)
    wifiAuth = models.CharField(max_length=8)
    wifiPass = models.CharField(max_length=28)
    
    def create(self, _wifiname, _wifiauth, _wifipass):
        self.wifiName = _wifiname
        self.wifiAuth = _wifiauth
        self.wifiPass = _wifipass

    def __str__(self):
        return self.wifiName + ' ' + self.wifiAuth + ' ' + self.wifiPass


class SmsModel(models.Model):
    textmessage = models.CharField(max_length = 26)
    number = models.CharField(max_length=8)

    def create(self, _textmessage, _number):
        self.textmessage = _textmessage
        self.number = _number

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
        #img.save("C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\media\\code.png")

        #kasper
        img.save("C:\\Users\\Skynet\\Desktop\\QR_app\\qr_app\\media\\code.png")
            
