from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def Ehub(request):
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())



def loading(request):
  template = loader.get_template('loading.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


