from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<amfisymbol>[0-9]{6})/(?P<startdate>[0-9]{8})/(?P<enddate>[0-9]{8})/$', views.navjson, name='navjson'),
]
