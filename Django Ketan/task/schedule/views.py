from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse ('Good Morning')

# Create your views here.
