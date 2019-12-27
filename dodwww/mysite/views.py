from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mysite.models import Store, Drinks
import json

def index(request):
	
	return render(request, "index.html")

def query(request, qstr="none"):
    
    if qstr == 'allstores':
        allstores = Store.objects.all()
        res = list(allstores.values())
    else:
        res = {'key':'none'}

    return JsonResponse(res, safe=False)