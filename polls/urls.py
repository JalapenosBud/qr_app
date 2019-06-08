from django.urls import path, include

from . import views
 
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('weblink/', views.weblink, name='weblink'),
    path('sms/', views.sms, name='sms'),
    path('wifi/', views.wifi, name='wifi')
]
