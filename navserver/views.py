from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader

from .models import MutualFund, MutualFundNAV

def index(request):
    mflist = MutualFund.objects.order_by('-mfname')
    template = loader.get_template('navserver/index.html')
    context = {
        'mflist': mflist,
        'startdate': '20150814',
        'enddate': '20160814',
    }
    return HttpResponse(template.render(context, request))

def navlist(amfisymbol, startdate, enddate):
    try:
        mf = MutualFund.objects.get(amfisymbol=amfisymbol)
    except:
        raise Http404("MF does not exist!")

    hyphenate_date = lambda x : x[:4] + '-' + x[4:6] + '-' + x[6:]
    startdate = hyphenate_date(startdate)
    enddate = hyphenate_date(enddate)
    nav_values = mf.nav.filter(date__range = (startdate, enddate)).order_by('date')
    return list(nav_values.values('date', 'nav'))

def navjson(request, amfisymbol, startdate, enddate):
    return JsonResponse(navlist(amfisymbol, startdate, enddate), safe=False)

def lumpsumcompare(request, amfisymbol1, amfisymbol2, startdate, enddate):
    nav_list_1 = navlist(amfisymbol1, startdate, enddate)
    nav_list_1_multiple = 10000.0 / float(nav_list_1[0]['nav'])
    print(nav_list_1[0]['nav'])
    print(nav_list_1_multiple)
    nav_list_1 = [{"date" : i['date'],
                       'value' : '{:.2f}'.format(nav_list_1_multiple * float(i['nav']))}
                       for i in nav_list_1]
    nav_list_2 = navlist(amfisymbol2, startdate, enddate)
    nav_list_2_multiple = 10000.0 / float(nav_list_2[0]['nav'])
    print(nav_list_2[0]['nav'])
    print(nav_list_2_multiple)
    print(nav_list_2_multiple * float(nav_list_2[0]['nav']))
    nav_list_2 = [{"date" : i['date'],
                       'value' : '{:.2f}'.format(nav_list_2_multiple * float(i['nav']))}
                       for i in nav_list_2]
    return JsonResponse([nav_list_1, nav_list_2], safe=False)

def navview(request, amfisymbol, startdate, enddate):
    try:
        mf = MutualFund.objects.get(amfisymbol=amfisymbol)
    except:
        raise Http404("MF does not exist!")
    template = loader.get_template('navserver/navview.html')
    context = {
        'amfisymbol' : amfisymbol,
        'mfname' : mf.mfname,
        'startdate' : startdate,
        'enddate' : enddate,}
    return HttpResponse(template.render(context, request))

def lumpsumview(request, amfisymbol1, amfisymbol2, startdate, enddate):
    try:
        mf1 = MutualFund.objects.get(amfisymbol=amfisymbol1)
        mf2 = MutualFund.objects.get(amfisymbol=amfisymbol2)
    except:
        raise Http404("MF does not exist!")
    template = loader.get_template('navserver/navcompare.html')
    context = {
        'amfisymbol1' : amfisymbol1,
        'mfname1' : mf1.mfname,
        'amfisymbol2' : amfisymbol2,
        'mfname2' : mf2.mfname,
        'startdate' : startdate,
        'enddate' : enddate,}
    return HttpResponse(template.render(context, request))
    
