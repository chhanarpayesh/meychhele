from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^list/$', views.CinemaListView.as_view(), name='list'),
    url(r'^list/(?P<slug>[\w\s-]+)/$', views.CinemaListView.as_view(), name='verify'),
    url(r'^create/$', views.CinemaCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/edit/$', views.CinemaUpdateView.as_view(), name='edit'),
    url(r'^designshots/$', views.DesignListView.as_view(), name='designshots'),
    url(r'^designshots/(?P<pk>\d+)/$', views.DesignShotUpdateView.as_view(), name='designshots'),
    url(r'^createdesignshot/$', views.DesignShotCreateView.as_view(),name='createdesignshot'),
    url(r'^foodshots/$', views.FoodListView.as_view(), name='foodshots'),
    url(r'^foodshots/(?P<pk>\d+)/$', views.FoodShotUpdateView.as_view(), name='foodshots'),
    url(r'^createfoodshot/$', views.FoodShotCreateView.as_view(),name='createfoodshot'),
    url(r'^locationshots/$', views.LocationListView.as_view(), name='locationshots'),
    url(r'^locationhots/(?P<pk>\d+)/$', views.LocationShotUpdateView.as_view(), name='locationshots'),
    url(r'^createlocationshot/$', views.LocationShotCreateView.as_view(),name='createlocationshot'),
    url(r'^beginnings/$', views.BeginningsListView.as_view(), name='beginnings'),
    url(r'^beginnings/(?P<pk>\d+)/$', views.BeginningsUpdateView.as_view(), name='beginnings'),
    url(r'^createbeginning/$', views.BeginningsCreateView.as_view(),name='createbeginning'),
    url(r'^endings/$', views.EndingsListView.as_view(), name='endings'),
    url(r'^endings/(?P<pk>\d+)/$', views.EndingsUpdateView.as_view(), name='endings'),
    url(r'^createending/$', views.EndingsCreateView.as_view(),name='createending'),
    url(r'^(?P<slug>[\w-]+)/$', views.CinemaDetailView.as_view(), name='detail'),
]