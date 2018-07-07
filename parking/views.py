from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from parking.models import Parking, Zone, Place
from .forms import ParkingForm, ZoneForm, PlaceForm
from django.http import HttpResponse
import string


def parking_choice(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('parking_list')
            print('choice = ', choice)
            query = Zone.objects.filter(parking__description=choice)
            #print('query = ', query)
            #form = ZoneForm(query=query)
            pk = Parking.objects.get(description=choice).pk
            if not query:
                return HttpResponse('Ваша парковка не содержит зон')
            return redirect('parking:zone_choice', pk=pk)
    else:
        form = ParkingForm()
    return render(request, 'parking/parking_choice.html', {'form': form})


def zone_choice(request, pk):
    if request.method == "POST":
        form = ZoneForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('zone_list')
            #query = Place.objects.filter(zone__description=choice)
            #print(query)
            zone_id = Zone.objects.get(description=choice).zone_id
            #print('zone_id = ', zone_id)
            return redirect('parking:place_choice', zone_id=zone_id, pk=pk)
    else:
        print('parking pk = ', pk)
        query = Zone.objects.filter(parking__pk=pk)
        form = ZoneForm(query=query)

        return render(request, 'parking/zone_choice.html', {'form': form})


def place_choice(request, zone_id, pk):
    if request.method == "POST":
        print('request post??')
        form = PlaceForm(request.POST)
        if form.is_valid():
            print('valid?')
            choice = form.cleaned_data.get('place_list')
            print('wtf ', choice)
            choice.is_free = not choice.is_free
            choice.save()
            pl = choice
            print('IS IT REAL OMG', pl.zone.zone_id, ' ', pl.number, ' ', pl.is_free)
            query = Place.objects.filter(zone__zone_id=zone_id)
            form = PlaceForm(query=query)
        query = Place.objects.filter(zone__zone_id=zone_id)
        form = PlaceForm(query=query)
        return render(request, 'parking/place_choice.html', {'form': form, 'pk': pk})
    else:
        query = Place.objects.filter(zone__zone_id=zone_id)
        print('places query = ', query)
        form = PlaceForm(query=query)
    return render(request, 'parking/place_choice.html', {'form': form, 'pk': pk})
