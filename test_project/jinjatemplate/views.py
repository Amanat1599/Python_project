from django.shortcuts import render
# Create your views here.


def jinjatemplate(request):
    context={"first_name":"Geek","last_name":"For Geek"}
    return render(request,"jintemplate\index.html")