# views.py
import os
import vobject
import pyqrcode
import png

from django.shortcuts import render
from .forms import NameForm
from pathlib import Path
from .models import FileHandler
from .forms import SmsForm, VCard
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from QRCODE.settings import BASE_DIR


def index(request):
        pass


def weblink(request):
    context = {}

    return render(request, 'polls/weblink.html',context)

def loadfile(request):
        
        context = {}
        return render(request, 'polls/loadfile.html', context)

def sms(request):
        context = {}
        file_path = os.path.join(BASE_DIR, 'media/')
        name_form = NameForm(request.POST or None, initial={'textmessage': 'whatever'}, use_required_attribute=False)

        smsform = SmsForm()
        smsform.number = request.POST.get('number')
        smsform.name = request.POST.get('textmessage')
        #TODO: take input fields
        if request.method == 'POST':
                QRCode = pyqrcode.create(F'sms:+4530563053:hello%20rick%20and%20morty%20fanclub.')
                QRCode.png(file_path + 'code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
                
                return render(request, 'polls/sms.html', context)
        else:
                return render(request, 'polls/sms.html', context)
        #return render(request, 'polls/sms.html', {'name_form': name_form})

def wifi(request):
        context = {}
        if request.method == 'POST':
                
                #TODO: input fields in html for wifi info
                Wifi_Name = 'WiFimodem-94F5'
                Wifi_Protocol = 'WPA/WPA2'
                Wifi_Password = 'FooBarBaz'
                QRCode = pyqrcode.create(F'WIFI:T:{Wifi_Protocol};S:{Wifi_Name};P:{Wifi_Password};;')
                #TODO: ret path til media folder
                QRCode.png('~/Documents/pythonstuff/qr_app/media\\media\\code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
                #path = default_storage.save('/media/', ContentFile(QRCode))
                #QRCode.show()
                return render(request, 'polls/wifi.html', context)
        else:
                return render(request, 'polls/wifi.html', context)