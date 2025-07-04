from django.http import HttpResponse
from django.shortcuts import render



def simple_view (request):
    return render(request,'home.html')


