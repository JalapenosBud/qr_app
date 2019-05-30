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
def index(request):
    name_form = NameForm(request.POST or None, initial={'name': 'whatever'}, use_required_attribute=True)
    context = {}
      
    if request.method == 'POST':
        if name_form.is_valid():
            # do something
            #FileHandler().savenewfile(name_form.cleaned_data['name'])
            FileHandler().generateQR(name_form.cleaned_data['name'])
            #print("running this")
        #return render(request, 'polls/index.html', {'name_form': name_form})
    else: 
        name_form = NameForm()
    return render(request, 'polls/index.html', {'name_form': name_form})

   # return render(request, 'polls/index.html', context)


def weblink(request):
    name_form = NameForm(request.POST or None, initial={'name': 'whatever'}, use_required_attribute=False)
   
    context = {}
    if request.method == 'POST':
        if name_form.is_valid():
            # do something
            FileHandler().savenewfile(name_form.cleaned_data['name'])
            FileHandler().generateQR(name_form.cleaned_data['name'])
            #print("running this")
        #return render(request, 'polls/weblink.html', {'name_form': name_form})
    else: 
        name_form = NameForm()
    return render(request, 'polls/weblink.html', {'name_form': name_form})

def loadfile(request):
        
        context = {}

        if request.method == 'POST':
                module_dir = os.path.dirname(Path(__file__).resolve().parent)
                file_path = os.path.join(module_dir, 'file.txt')   #full path to text.
                data_file = open(file_path , 'r')
                data = data_file.read()
                context = {'rooms': data}
                FileHandler().generateQR(data)
                return render(request, 'polls/loadfile.html', context)
        else:
                return render(request, 'polls/loadfile.html', context)

def sms(request):
        name_form = NameForm(request.POST or None, initial={'name': 'whatever'}, use_required_attribute=False)

        smsform = SmsForm()
        #TODO: change name to textmessage
        smsform.name = request.POST.get('name')
        smsform.number = request.POST.get('number')
        #TODO: take input fields
        #QRCode = pyqrcode.create(F'sms:+4530563053:wubba%20lubba%20wub%20wub%20ballsack.')
        context = {}
        return render(request, 'polls/sms.html', {'name_form': name_form})

def wifi(request):
        context = {}
        if request.method == 'POST':
                
                #TODO: input fields in html for wifi info
                Wifi_Name = 'WiFimodem-94F5'
                Wifi_Protocol = 'WPA/WPA2'
                Wifi_Password = 'FooBarBaz'
                QRCode = pyqrcode.create(F'WIFI:T:{Wifi_Protocol};S:{Wifi_Name};P:{Wifi_Password};;')
                #TODO: ret path til media folder
                QRCode.png('C:\\Users\\Jalap\\Documents\\QRCODE\\QRCODE\\media\\code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
                #path = default_storage.save('/media/', ContentFile(QRCode))
                QRCode.show()
                return render(request, 'polls/wifi.html', context)
        else:
                return render(request, 'polls/wifi.html', context)