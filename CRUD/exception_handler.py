from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework import status
from CRUD.settings import DEBUG
from django.template import loader, RequestContext, Context
from django.core.exceptions import PermissionDenied


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response:
        exc = APIException(exc)
        response = exception_handler(exc, context)

    if response is not None:
        error_message = response.data['detail']
        response.data.pop('detail', {})
        response.data['status'] = str(response.status_code)
        response.data['message'] = error_message
        response.data['detail'] = exc.default_detail
        response.data['status_text'] = response.status_text
        response.data['exception'] = exc.__class__.__name__

    return response


def error_404(request, exception):
    message = 'End point not-found error'
    response = JsonResponse(data={'message': message, 'status_code': 404})
    response.status_code = 404
    return response


def error_500(request):
    message = 'An error occurred, its on us'
    response = JsonResponse(data={'message': message, 'status_code': 500})
    response.status_code = 500
    return response
