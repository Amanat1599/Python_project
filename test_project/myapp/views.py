from django.shortcuts import render
from django.http import HttpResponse

# class members():
#     print("Hellow world")


def membersapp(request):
    print('Print in view in it')
    return HttpResponse("IN View")