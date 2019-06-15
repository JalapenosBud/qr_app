import os
#import pyqrcode
import png
import json
#import io
#import sys

#from django.core import serializers
from pathlib import Path
from .models import SmsModel, WifiModel, WeblinkModel, generate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseBadRequest
from django.forms.models import model_to_dict
#from pprint import pprint
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
#from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'polls/index.html')
    
def weblink(request):
        if request.method == 'GET':
                return render(request, "polls/weblink.html")

        if request.method == 'POST':
                if '_load' in request.POST:
                        try:
                                weblink = WeblinkModel.objects.all().last()
                        except:
                                raise Http404('Requested wifi model not found')

                        context = {'weblink': weblink.weblink}
                        return render(request, 'polls/weblink.html',context) 


                if '_generate_save' in request.POST:
                        generate(request.POST["weblink"])
                        model = WeblinkModel()
                        model.create(request.POST["weblink"])
                        model.save()

                        with open('C:\\Users\\Skynet\\Desktop\\QR_app\\qr_app\\media\\weblinkdata.json', 'w') as outfile:
                                json.dump(model_to_dict(model), outfile)
                
                        context = {
                                'object': model
                        }

                if '_upload' in request.POST:
                        json_file = request.FILES['document']
                        bytestream = json_file.read()
                        data = json.loads(bytestream)
                        weblink = data['weblink']
                        context = {
                                'weblink': weblink
                        }
                return render(request, 'polls/weblink.html',context)

        return HttpResponseBadRequest()

def wifi(request):
        if request.method == 'GET':
                return render(request, "polls/wifi.html")
        
        if request.method == "POST":
                if '_load' in request.POST:
                        try:
                                WiFi = WifiModel.objects.all().last()
                        except:
                                raise Http404('Requested wifi model not found')

                        context = {'wifiname': WiFi.wifiName,
                                'wifiauth': WiFi.wifiAuth,
                                'wifipass': WiFi.wifiPass}
                        return render(request, 'polls/wifi.html',context) 

                if '_generate_save' in request.POST:
                        _wifiauth = request.POST["wifi-auth"]
                        _wifiname = request.POST["wifi-name"]
                        _wifipass = request.POST["wifi-pass"]
                        
                        model = WifiModel()

                        userInput = f"WIFI:T:{_wifiauth};S:{_wifiname};P:{_wifipass};;"
                        generate(userInput) 
                
                        #MODEL CREATION
                        
                        model.create(_wifiname, _wifiauth, _wifipass)
                        model.save()

                        #MAKE MODEL INTO DICT
                        with open('C:\\Users\\Skynet\\Desktop\\QR_app\\qr_app\\media\\wifidata.json', 'w') as outfile:
                                json.dump(model_to_dict(model), outfile)
                
                        return render(request, 'polls/wifi.html') 

                if '_upload' in request.POST:
                        json_file = request.FILES['document']
                        bytestream = json_file.read()

                        data = json.loads(bytestream)
                        
                        wifiname =     data['wifiName']
                        wifiprotocol = data['wifiAuth']
                        wifipass =     data['wifiPass']
                        context = {'wifiname': wifiname,
                                   'wifiauth': wifiprotocol,
                                   'wifipass': wifipass}
                return render(request, 'polls/wifi.html', context)
        return HttpResponseBadRequest() 


def sms(request):
        if request.method == 'GET':
                return render(request, "polls/sms.html")

        if request.method == "POST":
                if '_load' in request.POST:
                        try:
                                sms = SmsModel.objects.all().last()
                        except:
                                raise Http404('Requested sms model not found')
                        context = {
                                'textmessage': sms.textmessage,
                                'number': sms.number
                        }
                        return render(request, 'polls/sms.html', context)

                if '_generate_save' in request.POST:
                        #MODEL CREATION
                        model = SmsModel()
                        model.create(request.POST["textmessage"], request.POST["number"])
                        model.save()

                        #MAKE MODEL INTO DICT
                        with open('C:\\Users\\Skynet\\Desktop\\QR_app\\qr_app\\media\\smsdata.json', 'w') as outfile:
                                json.dump(model_to_dict(model), outfile)
                
                        _textmessage = request.POST["textmessage"]
                        _number = request.POST["number"]
 
                        generate(F'sms:{_number}:{_textmessage}.')
                        return render(request, 'polls/sms.html') 

                if '_upload' in request.POST:
                        json_file = request.FILES['document']
                        bytestream = json_file.read()

                        data = json.loads(bytestream)
                        
                        _textmessage = data['textmessage']
                        _number = data['number']
                        context = {'textmessage': _textmessage,
                                'number': _number}
                        #return render(request, 'polls/sms.html', context)
                return render(request, 'polls/sms.html', context)
        return HttpResponseBadRequest() 