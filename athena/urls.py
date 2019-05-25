from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^list/$', views.AthenaListView.as_view(), name='list'),
    url(r'^list/all/$', views.AthenaListAllView.as_view(), name='listall'),
    url(r'^create/$', views.AthenaCreateView.as_view(),name='create'),
    url(r'^$', views.AthenaRankListView.as_view(), name='rank'),
    url(r'^rank/$', views.AthenaRankListView.as_view(), name='rank'),
    url(r'^createrank/$', views.AthenaRankCreateView.as_view(),name='createrank'),
    url(r'^(?P<slug>[\w-]+)/$', views.AthenaDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.AthenaUpdateView.as_view(), name='update'),
    url(r'^rank/(?P<slug>\d+)/edit/$', views.AthenaRankUpdateView.as_view(), name='updaterank'),
    url(r'^list/(?P<slug>[\w\s-]+)/$', views.AthenaListView.as_view(), name='roots'),
]