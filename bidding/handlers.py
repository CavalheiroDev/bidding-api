from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import exception_handler

from utils.utils import ErrorsFormatter


def exception_errors_format_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return response

    formatter = ErrorsFormatter(exc)

    response.data = formatter()

    return response
