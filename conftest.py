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
