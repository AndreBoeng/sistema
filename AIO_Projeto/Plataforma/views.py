from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Plataforma(request):
    return render(request, 'base.html' )