from django.urls import path

from . import views

urlpatterns = [
    path("template",views.jinjatemplate,name="all")
]
