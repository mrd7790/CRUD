import http.client

from django.http import JsonResponse


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        # # error message
        # if response.status_code != 200:
        #     data = {
        #         'status': str(response.status_code),
        #         'message': str(response.reason_phrase),
        #     }
        #     return JsonResponse(data)

        if response.status_code == 404:
            data = {
                    'status': str(response.status_code),
                    'message': str(response.reason_phrase),
                }
            return JsonResponse(data)

        return response
