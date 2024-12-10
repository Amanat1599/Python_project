from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# class members():
#     print("Hellow world")


def membersapp(request):
    print('Print in view in it')
    return HttpResponse("IN View")



def ExceptionView(request):
    print('Print in Exception view in it')
    a=10/0
    return HttpResponse("IN Exception View")



def TemplateView(request):
    print('Print in Template view in it')
    context={"name":"My_name"}
    return TemplateResponse(request,"index.html",context)

# def TemplateResponse(request):
#     print('In templateResponse : ')
