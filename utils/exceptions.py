from rest_framework import status
from rest_framework.exceptions import ValidationError


class BiddingValidationError(ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST

    def _init_(self, message=None, code=None, status_code: int = status_code):
        if status_code != self.status_code:
            self.status_code = status_code

        self.error_message = message

        super()._init_(detail=message, **{"code": code} if code else {})


class ObjectNotFound(BiddingValidationError):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
