from django.shortcuts import render
from django.core import serializers
from .models import Alumno
from django.http import HttpResponse
from django.template import loader, Context
from .forms import LoginForm

# Create your views here.
def index(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = request.POST['username']
        password = request.POST['password']
        print(user, password)




    context = { 
        'form': form
    }
    return render(request, 'alumno/index.html', context)


def wsListMike(request):
    data = serializers.serialize('json', Alumno.objects.all())
    return HttpResponse(data, content_type='application/json')
