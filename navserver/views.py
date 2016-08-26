from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import MutualFund, MutualFundNAV

def index(request):
    return HttpResponse("Hello, world. You're at the NAV server index.")

def navjson(request, amfisymbol, startdate, enddate):
    try:
        mf = MutualFund.objects.get(amfisymbol=amfisymbol)
    except:
        raise Http404("MF does not exist!")

    hyphenate_date = lambda x : x[:4] + '-' + x[4:6] + '-' + x[6:]
    startdate = hyphenate_date(startdate)
    enddate = hyphenate_date(enddate)
    nav_values = mf.nav.filter(date__range = (startdate, enddate))
    return JsonResponse(list(nav_values.values('date', 'nav')), safe=False)
