from django.urls import path, include

from . import views
 
app_name = 'qr_app'

urlpatterns = [
    # ex: /qr_app/
    path('', views.index, name='index'),
    path('weblink/', views.weblink, name='weblink'),
    path('sms/', views.sms, name='sms'),
    path('wifi/', views.wifi, name='wifi')
]
