from django.conf.urls import url

from . import views

app_name = 'navserver'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/(?P<amfisymbol>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.navjson, name='navjson'),
    url(r'^json/(?P<amfisymbol1>[0-9]{6}),(?P<amfisymbol2>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.lumpsumcompare, name='lumpsumcompare'),
    url(r'^v/(?P<amfisymbol1>[0-9]{6}),(?P<amfisymbol2>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.lumpsumview, name='lumpsumview'),
    url(r'^v/(?P<amfisymbol>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.navview, name='navview'),
]
