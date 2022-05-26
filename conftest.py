import pytest


@pytest.fixture
def authentication_user_invalid_credentials():
    return {'detail': 'No active account found with the given credentials'}


@pytest.fixture
def authentication_refresh_user_invalid_credentials():
    return {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
    }


@pytest.fixture
def error_message_create_user_with_username_already_exists():
    return {
        "errors": [
            {
                "message": "User with this username already exists",
                "code": "USER_ALREADY_EXISTS"
            }
        ]
    }


@pytest.fixture
def error_message_create_user_with_email_already_exists():
    return {
        "errors": [
            {
                "message": "User with this email already exists",
                "code": "USER_ALREADY_EXISTS"
            }
        ]
    }


@pytest.fixture
def error_message_create_user_with_empty_body():
    return {
        "errors": [
            {
                "message": "This field is required.",
                "code": "required",
                "field": "username"
            },
            {
                "message": "This field is required.",
                "code": "required",
                "field": "password"
            }
        ]
    }
