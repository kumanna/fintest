from django.conf.urls import url

from . import views

app_name = 'navserver'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<amfisymbol>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8}).json$', views.navjson, name='navjson'),
    url(r'^(?P<amfisymbol1>[0-9]{6}),(?P<amfisymbol2>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8}).json$', views.lumpsumcompare, name='lumpsumcompare'),
    url(r'^(?P<amfisymbol1>[0-9]{6}),(?P<amfisymbol2>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.lumpsumview, name='lumpsumview'),
    url(r'^(?P<amfisymbol>[0-9]{6})/(?P<startdate>[0-9]{8})-(?P<enddate>[0-9]{8})/$', views.navview, name='navview'),
]
