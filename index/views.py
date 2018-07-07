from django.shortcuts import render, HttpResponse
from parking.forms import *
from parking.models import *


# Create your views here.


def index(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)
        if form.is_valid():
            ch = form.cleaned_data.get('parking_list')
            print(ch)
            zones = Zone.objects.filter(parking__description=ch)
            print(zones)
            return HttpResponse(zones)
    else:
        form = ParkingForm()
        return render(request, 'index/index.html', {'form': form})
