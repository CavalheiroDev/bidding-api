from utils.exceptions import ObjectNotFound, BiddingValidationError


class UserNotFound(ObjectNotFound):
    DEFAULT_MESSAGE = 'User not found'
    DEFAULT_CODE = 'USER_NOT_FOUND'
    DEFAULT_STATUS_CODE = 404

    def __init__(self,
               message: str = DEFAULT_MESSAGE,
               code: str = DEFAULT_CODE,
               status_code: int = DEFAULT_STATUS_CODE):
        super().__init__(message=message, code=code, status_code=status_code)


class UserAlreadyExists(BiddingValidationError):
    DEFAULT_MESSAGE = 'User already exists'
    DEFAULT_CODE = 'USER_ALREADY_EXISTS'
    DEFAULT_STATUS_CODE = 400

    def __init__(self,
               message: str = DEFAULT_MESSAGE,
               code: str = DEFAULT_CODE,
               status_code: int = DEFAULT_STATUS_CODE):
        super().__init__(message=message, code=code, status_code=status_code)
