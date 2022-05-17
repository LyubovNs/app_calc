from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import venv



def homePageView(request):
    return HttpResponse('venv.main()')