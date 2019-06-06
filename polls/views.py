import os
import vobject
import pyqrcode
import png

from django.shortcuts import render
from pathlib import Path
from .models import SmsModel, WifiModel, WeblinkModel
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile
from django.http import HttpResponseBadRequest
from QRCODE.settings import BASE_DIR


def index(request):
    #context = {}
    return render(request, 'polls/index.html')
    
    
def weblink(request):
        if request.method == 'GET':
                return render(request, "polls/weblink.html")

        if request.method == 'POST':
                model = WeblinkModel()
                model.create(request.POST["weblink"])
                #model.weblink = request.POST["weblink"]
                #database save
                model.save()
                        #load methode kaldes her ()
                return render(request, 'polls/weblink.html')  
        return HttpResponseBadRequest()

def loadWeblink(request):
        if request.method == 'GET':
                print("HET")
                #model = WeblinkModel()
                #model.load("loadfile")
                return render(request, "polls/getone.html")


def wifi(request):
        if request.method == 'GET':
                return render(request, "polls/wifi.html")

        if request.method == 'POST':
                model = WifiModel()
                model.create(request.POST["wifi-name"], request.POST["wifi-pass"],request.POST["wifi-auth"])
                #model.wifi = request.POST["wifi"]
                model.save()
                return render(request, 'polls/wifi.html')
        return HttpResponseBadRequest() 


def sms(request):
        if request.method == 'GET':
                return render(request, "polls/sms.html")

        if request.method == 'POST':
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