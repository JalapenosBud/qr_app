from django.contrib import admin
from .models import WeblinkModel,WifiModel,SmsModel 

# Register your models here.
admin.site.register(WeblinkModel)
admin.site.register(WifiModel)
admin.site.register(SmsModel)