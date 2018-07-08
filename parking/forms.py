from django import forms
from .models import Parking, Zone, Place


class ParkingForm(forms.Form):

    class Meta:
        model = Parking

    parking_list = forms.ModelChoiceField(
        queryset=Parking.objects.all(),
        widget=forms.Select(attrs={'onChange': 'this.form.submit();'}),
        empty_label=''
    )


class ZoneForm(forms.Form):
    class Meta:
        model = Zone

    zone_list = forms.ModelChoiceField(
        queryset=Zone.objects.all(),
        widget=forms.Select(attrs={'onChange': 'this.form.submit();'}),
        empty_label=''
    )

    def __init__(self, *args, **kwargs):
        query = kwargs.pop('query', None)
        super(ZoneForm, self).__init__(*args, **kwargs)

        if query:
            self.fields['zone_list'].queryset = query


class PlaceForm(forms.ModelForm):
    number = forms.CharField(label='Номер', widget=forms.TextInput(
                 attrs={'size': '1'}))
    is_taken = forms.BooleanField(label='Занято', required=False)

    class Meta:
        model = Place
        fields = ('number', 'is_taken')

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['readonly'] = 'true'






# class PlaceForm(forms.Form):
#
#     place_list = forms.ModelChoiceField(
#         queryset=Place.objects.all(),
#         widget=forms.Select(attrs={'onChange': 'this.form.submit();'}),
#         empty_label=''
#
#     )
#
#     def __init__(self, *args, **kwargs):
#         query = kwargs.pop('query', None)
#         super(PlaceForm, self).__init__(*args, **kwargs)
#
#         if query:
#             self.fields['place_list'].queryset = query
#             # getting parking zone id of current query
#             print('here ', query)
#             z = query[0].zone.zone_id
#             self.initial['place_list'] = Place.objects.filter(zone__zone_id=z, is_free=False)

