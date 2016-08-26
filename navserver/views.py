from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import MutualFund, MutualFundNAV

def index(request):
    return HttpResponse("Hello, world. You're at the NAV server index.")

def navjson(request, amfisymbol, startdate, enddate):
    try:
        mf = MutualFund.objects.get(amfisymbol=amfisymbol)
    except:
        raise Http404("MF does not exist!")
    return HttpResponse("You asked for NAV data for %s from %s to %s."
                            % (amfisymbol, startdate, enddate))
