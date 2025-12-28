from django.shortcuts import render
from django.http import HttpResponse


def jan(request):
    return HttpResponse("Eat no meat for entire month")


def feb(request):
    return HttpResponse("Walk for 30 minutes everyday")
