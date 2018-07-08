from django.shortcuts import render, redirect
from parking.models import Parking, Zone, Place
from .forms import ParkingForm, ZoneForm, PlaceForm
from django.forms import modelformset_factory


def parking_choice(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('parking_list')
            pk = Parking.objects.get(description=choice).pk
            return redirect('parking:zone_choice', pk=pk)
        return render(request, 'parking/parking_choice.html', {'form': form})
    else:
        form = ParkingForm()
        return render(request, 'parking/parking_choice.html', {'form': form})


def zone_choice(request, pk):
    parking_name = Parking.objects.get(pk=pk).description
    if request.method == "POST":
        form = ZoneForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('zone_list')
            zone_id = Zone.objects.get(description=choice).zone_id
            return redirect('parking:place_choice', zone_id=zone_id, pk=pk)
        return render(request, 'parking/zone_choice.html', {'form': form, 'parking_name': parking_name})
    else:
        query = Zone.objects.filter(parking__pk=pk)
        form = ZoneForm(query=query)
        return render(request, 'parking/zone_choice.html', {'form': form, 'parking_name': parking_name})


def place_choice(request, zone_id, pk):
    placeformset = modelformset_factory(Place, form=PlaceForm, extra=0)
    parking_name = Parking.objects.get(pk=pk).description
    query = Place.objects.filter(zone__zone_id=zone_id)
    formset = placeformset(queryset=query)
    if request.method == "POST":
        formset = placeformset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('parking:place_choice', zone_id=zone_id, pk=pk)
        return render(request, 'parking/place_choice.html',
                      {'formset': formset, 'pk': pk, 'zone_id': zone_id, 'parking_name': parking_name})
    else:
        return render(request, 'parking/place_choice.html',
                      {'formset': formset, 'pk': pk, 'zone_id': zone_id, 'parking_name': parking_name})

