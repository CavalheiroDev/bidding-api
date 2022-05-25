from utils.exceptions import ObjectNotFound


class UserNotFound(ObjectNotFound):
    DEFAULT_MESSAGE = 'User not found'
    DEFAULT_CODE = 'USER_NOT_FOUND'
    DEFAULT_STATUS_CODE = 404

    def _init_(self,
               message: str = DEFAULT_MESSAGE,
               code: str = DEFAULT_CODE,
               status_code: int = DEFAULT_STATUS_CODE):
        super()._init_(message=message, code=code, status_code=status_code)
