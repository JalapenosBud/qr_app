import os
import pyqrcode
import png
import json

from django.core import serializers
from django.shortcuts import render
from pathlib import Path
from .models import SmsModel, WifiModel, WeblinkModel
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseBadRequest
from django.forms.models import model_to_dict
from pprint import pprint
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
                        model.create(request.POST["weblink"])
                        model.save()
                        return render(request, 'polls/weblink.html')
                if '_save' in request.POST:
                        
                        model = WeblinkModel()
                        model.create(request.POST["weblink"])
                        model.save()

                        dict_obj = model_to_dict(model)
                        serialized = json.dumps(dict_obj)

                        with open('data.json', 'w') as outfile:
                                json.dump(serialized, outfile)
                
                        context = {'object': model}
                if '_populate' in request.POST:
                        with open('data.json', "r") as fp:
                                somedata = json.load(fp)
                        pprint(somedata)

                        context = {'object': somedata}
                return render(request, 'polls/weblink.html',context)    
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
                        model.save()
                        return render(request, 'polls/wifi.html') 
                
                if '_save' in request.POST:
                        
                        model = WifiModel()
                        model.create(request.POST["wifi-name"], request.POST["wifi-pass"],request.POST["wifi-auth"])
                        model.save()

                        dict_obj = model_to_dict(model)
                        #serialized = json.dumps(dict_obj)
                        with open('data.json', 'w') as outfile:
                                json.dump(dict_obj, outfile)
                
                        context = {'object': model}
                        return render(request, 'polls/wifi.html') 
                        
                if '_populate' in request.POST:
                        with open('data.json') as data_file:
                                somedata = json.loads(data_file.read())
                        #wifiname = json.loads(somedata['id'][0])

                        wifiname =     somedata['wifiName']
                        wifiprotocol = somedata['wifiPass']
                        wifipass =     somedata['wifiAuth']
                        context = {'wifiname': wifiname,
                                   'wifiauth': wifiprotocol,
                                   'wifipass': wifipass}
                        return render(request, 'polls/wifi.html',context)                
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
                        return render(request, 'polls/sms.html', context)
                if '_generate' in request.POST:
                        model = SmsModel()
                        model.create(request.POST['textmessage'],request.POST['number'])
                        model.save()
                        return render(request,'polls/sms.html')        
        return HttpResponseBadRequest() 

def showImage(request):
        link = "C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\media\\code.png"
        if request.method == 'GET':
                pass



def savefile(request, model, templatestring):
    objects = model.objects.all()
    with open(r'C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\file.json', "w") as out:
        mast_point = serializers.serialize("json", objects)
        out.write(mast_point)
    template = loader.get_template(templatestring)
    context = {'object': objects}
    return HttpResponse(template.render(context, request))
    
#def image_to_html(image):
  #  return '<img src="%(path)s" title="%(title)s" alt="%(alt)s" />' % {
     #   'path': image.raw.path,
    #    'title': image.title,
     #   'alt': image.alt_text
   # }     

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError