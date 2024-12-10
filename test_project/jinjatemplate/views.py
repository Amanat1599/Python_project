from django.shortcuts import render

# Create your views here.


def jinjatemplate(request):
    return render(request,"index.html")