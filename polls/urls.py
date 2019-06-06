from django.urls import path, include

from . import views
 
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('loadfile/', views.loadfile, name='loadfile'),
    path('weblink/', views.weblink, name='weblink'),
    path('sms/', views.sms, name='sms'),
]
