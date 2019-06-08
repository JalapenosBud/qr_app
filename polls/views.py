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
                        pass
                       # model = WeblinkModel()
                      #  model.create(request.POST["weblink"])
                       # data = WeblinkModel.objects.all()

                        #for item in data:
                        #        item['weblink'] = model_to_dict(item['weblink'])

                       # return HttpResponse(json.dumps(data), mimetype='application/json')

                       # with open(r'C:\\Users\\Jalap\\Desktop\\qr\\qr_app\\file.json', "w") as out:
                                #mast_point = serializers.serialize("json", model)
                                #out.write(mast_point)
                                #json.dump(model,out)
                        #context = {'object': model}
                        #savefile(request, SmsModel, 'polls/weblink.html')
                        #data = serializers.serialize('json', WeblinkModel.objects.all())
                        #return render(request, 'polls/weblink.html')  
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
