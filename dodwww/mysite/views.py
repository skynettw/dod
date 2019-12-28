from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mysite.models import Store, Drinks
import json

def index(request):
	
	return render(request, "index.html")

def store(request, storename='7-11'):
    try:
        s = Store.objects.get(name=storename)
    except:
        s = Store.objects.get(name='7-11')
    alldrinks = Drinks.objects.filter(store=s)
    res = list(alldrinks.values())

    return JsonResponse(res, safe=False)

def query(request, qstr="none"):
    
    if qstr == 'allstores':
        allstores = Store.objects.all()
        res = list(allstores.values())
    elif qstr == 'alldrinks':
        alldrinks = Drinks.objects.all()
        res = list(alldrinks.values())
    else:
        res = {'key':'none'}

    return JsonResponse(res, safe=False)