from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.utils import swagger_auto_schema

from bidding.authentication.serializers import (
    UserAuthInputSerializer,
    UserAuthOutputSerializer,
    UserAuthRefreshInputSerializer,
    UserAuthRefreshOutputSerializer
)


class UserAuthAPIView(TokenObtainPairView):

    @swagger_auto_schema(
        request_body=UserAuthInputSerializer,
        responses={200: UserAuthOutputSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserAuthRefreshAPIView(TokenRefreshView):

    @swagger_auto_schema(
        request_body=UserAuthRefreshInputSerializer,
        responses={200: UserAuthRefreshOutputSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
