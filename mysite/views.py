__author__ = 'yinqiwei'
from django.shortcuts import render
from django.http import HttpResponse


def hellow(request):
    return HttpResponse("hellow world")
