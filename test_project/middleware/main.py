
from typing import Any
from django.shortcuts import HttpResponse

class ExampleMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('This is one time initilization of Example middleware')

    def __call__(self, request):

        print("This is Example before view")

        response = self.get_response(request)
        print("This is Example after view")
       

        return response
    
class FirstMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("This is one time initilization in First middle ware")

    def __call__(self, request):
        print("This is First before view")
        response = self.get_response(request)
        #response=HttpResponse("Get Out")
        print("This is First after view")
        return response
    
class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(requets,*args,**kwargs):
        print("In Process View")
        #return None
        return HttpResponse("Process View this is just before view.")
    
    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        print("In exception View")
        msg=exception
        print(msg)
        return HttpResponse(msg)



class MyTemplateMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_template_response(self,request,exception):
        print("In process template")
        pass