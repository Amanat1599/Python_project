

class ExampleMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Hellow world in middleware")

        response = self.get_response(request)
        user_agent=request.META.get('HTTP_USER_AGENT')
        print("***")
        user_agent
        print("*****")

        return response
    


class FirstMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("FIrst Hellow world in middleware")
        response = self.get_response(request)
        return response
    