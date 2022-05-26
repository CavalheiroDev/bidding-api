import pytest


@pytest.fixture
def authentication_user_invalid_credentials():
    return {
        "errors": [
            {
                "message": "No active account found with the given credentials",
                "code": "no_active_account"
            }
        ]
    }


@pytest.fixture
def authentication_refresh_user_invalid_credentials():
    return {
        "errors": [
            {
                "message": "Token is invalid or expired",
                "code": "token_not_valid",
                "field": "detail"
            },
            {
                "message": "token_not_valid",
                "code": "token_not_valid",
                "field": "code"
            }
        ]
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
