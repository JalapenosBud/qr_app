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

from django.template.loader import TemplateDoesNotExist

from django.http import HttpResponse, Http404
from .models import WeblinkModel

def index(request):
    #context = {}
    return render(request, 'polls/index.html')
    
    
def weblink(request):
        if request.method == 'GET':
                return render(request, "polls/weblink.html")

        if request.POST:
                if '_load' in request.POST:
                        #do_load()
                        print('load')
                        try:
                                web = WeblinkModel.objects.all().first()
                                #order_by('weblink').first()
                        except:
                                raise Http404('Requested weblink model not found')
                        #my_weblink = web.weblink.
                       # template = get_template('weblink.html')
                        #getfirst = web.order_by('weblink').first()
                        context = {'weblink':web}
                        print(context)
                        #output = type.render(variables)
                        return render(request, 'polls/weblink.html', context)
                elif '_generate' in request.POST:
                        print('generate')
                        model = WeblinkModel()
                        model.create(request.POST["weblink"])# model.weblink = request.POST["weblink"]# database save
                        model.save()# load methode kaldes her()
                        return render(request, 'polls/weblink.html')
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


#def user_page(request, username):
     #   try:
      # #         user = User.objects.get(username = username)
      #  except:
      #          raise Http404('Requested user not found.')
##
      ##  product = user.product_set.all()
       # template = get_template('user_page.html')
       # variables = Context({
        #        'username': username,
        #        'product': product
     #   })
       # output = template.render(variables)
      #  return HttpResponse(output)

