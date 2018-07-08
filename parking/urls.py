from django.conf.urls import url
from . import views


app_name = 'parking'
urlpatterns = [
    url(r'^$', views.parking_choice, name='parking_choice'),
    url(r'^(?P<pk>\d+)/$', views.zone_choice, name='zone_choice'),
    url(r'^(?P<pk>\d+)/(?P<zone_id>\w)/$', views.place_choice, name='place_choice'),
]
