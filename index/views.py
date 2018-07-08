from django.shortcuts import render, HttpResponse
from parking.forms import *
from parking.models import *


# Create your views here.


def index(request):
    return render(request, 'index/index.html')
