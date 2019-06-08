import os
import vobject
import pyqrcode
import png

from django.core import serializers
from django.shortcuts import render
from pathlib import Path
from .models import SmsModel, WifiModel, WeblinkModel
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile
from django.http import HttpResponseBadRequest
from QRCODE.settings import BASE_DIR

from django.forms.models import modelform_factory
from django.template.loader import TemplateDoesNotExist

from django.http import HttpResponse, Http404
from .models import WeblinkModel

def index(request):
    #context = {}
    return render(request, 'polls/index.html')
    
    
def weblink(request):
        if request.method == 'GET':
                return render(request, "polls/weblink.html")

        if request.method == 'POST':
                if '_load' in request.POST:
                        try:
                                web = WeblinkModel.objects.all().last()
                        except:
                                raise Http404('Requested weblink model not found')
                        context = {'weblink':web}
                        return render(request, 'polls/weblink.html', context)
                if '_generate' in request.POST:
                        model = WeblinkModel()
                        model.create(request.POST["weblink"])# model.weblink = request.POST["weblink"]# database save
                        model.save()# load methode kaldes her()
                        return render(request, 'polls/weblink.html')
                if '_save' in request.POST:
                        data = serializers.serialize('json', WeblinkModel.objects.all())
                return render(request, 'polls/weblink.html')    
        return HttpResponseBadRequest()

def wifi(request):
        if request.method == 'GET':
                return render(request, "polls/wifi.html")
        
        if request.POST:
                if '_load' in request.POST:
                        try:
                                wifi = WifiModel.objects.all().last()
                        except:
                                raise Http404('Requested wifi model not found')
                        context = {'wifiname': wifi.wifiName,
                                   'wifipass': wifi.wifiPass,
                                   'wifiauth': wifi.wifiAuth}
                        return render(request, 'polls/wifi.html', context)
                if '_generate' in request.POST:
                        model = WifiModel()
                        model.create(request.POST["wifi-name"], request.POST["wifi-pass"],request.POST["wifi-auth"])
                        #model.wifi = request.POST["wifi"]
                        model.save()
                        return render(request, 'polls/wifi.html')                
        return HttpResponseBadRequest() 


def sms(request):
        if request.method == 'GET':
                return render(request, "polls/sms.html")

        if request.POST:
                if '_load' in request.POST:
                        try:
                                sms = SmsModel.objects.all().last()
                        except:
                                raise Http404('Requested sms model not found')
                        context = {'textmessage': sms.textmessage,
                                'number': sms.number}
                        #print(sms)
                        return render(request, 'polls/sms.html', context)
                if '_generate' in request.POST:
                        model = SmsModel()
                        model.create(request.POST['textmessage'],request.POST['number'])
                        #model.wifi = request.POST["sms"]
                        model.save()
                        return render(request,'polls/sms.html')        
        return HttpResponseBadRequest() 


def getOne(request, type, id):
        #jeres detaljer er her omkring den specfikke QR Code.
        qr = get_object_or_404(type, pk=id)
        if request.method == 'GET':
                context = {"qr": qr, "type": type}
                #"getone.html" er ikke lavet men den skal udfylde 
                return render(request, "polls/getone.html", context)

def showImage(request):
        link = "C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\media\\code.png"
        if request.method == 'GET':
                pass

#def image_to_html(image):
  #  return '<img src="%(path)s" title="%(title)s" alt="%(alt)s" />' % {
     #   'path': image.raw.path,
    #    'title': image.title,
     #   'alt': image.alt_text
   # }     
