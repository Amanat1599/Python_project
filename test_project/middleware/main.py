
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
        #response = self.get_response(request)
        response=HttpResponse("Get Out")
        print("This is First after view")
        return response
    