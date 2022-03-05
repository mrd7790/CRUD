from django.http import Http404
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response:
        exc = APIException(exc)
        response = exception_handler(exc, context)

    if response is not None:
        error_message = response.data['detail']
        response.data.pop('detail', {})
        response.data['message'] = error_message
        response.data['status_code'] = response.status_code
        response.data['status_text'] = response.status_text
        response.data['exception'] = exc.__class__.__name__

    return response
