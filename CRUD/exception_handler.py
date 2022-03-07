from django.http import Http404, HttpResponse
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
