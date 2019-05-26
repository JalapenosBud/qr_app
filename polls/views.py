# views.py
import os
from django.shortcuts import render
from .forms import NameForm
from pathlib import Path
from .models import FileHandler

def index(request):
   
    context = {}
    
    return render(request, 'polls/index.html', context)


def weblink(request):
    name_form = NameForm(request.POST or None, initial={'name': 'whatever'}, use_required_attribute=False)
    context = {}
    if request.method == 'POST':
        if name_form.is_valid():
            # do something
            FileHandler().savenewfile(name_form.cleaned_data['name'])
        return render(request, 'polls/weblink.html', {'name_form': name_form})
    else: 
        return render(request, 'polls/weblink.html', context)

def loadfile(request):
        if request.method == 'GET':
                module_dir = os.path.dirname(Path(__file__).resolve().parent)
                file_path = os.path.join(module_dir, 'file.txt')   #full path to text.
                data_file = open(file_path , 'r')
                data = data_file.read()
                context = {'rooms': data}
        return render(request, 'polls/loadfile.html', context)
