from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from bidding.user.serializers import UserCreateAPIViewInputSerializer, UserCreateAPIViewOutputSerializer
from bidding.user.factories import make_user_creator_service

from bidding.mixins import ApiErrorsMixin


class UserCreateAPIView(APIView, ApiErrorsMixin):

    def __init__(self) -> None:
        self._user_creator = make_user_creator_service()

    @swagger_auto_schema(
        request_body=UserCreateAPIViewInputSerializer,
        responses={200: UserCreateAPIViewOutputSerializer}
    )
    def post(self, request):
        serializer = UserCreateAPIViewInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self._user_creator.create_user(data=serializer.validated_data)
        output = UserCreateAPIViewOutputSerializer(user)

        return Response(output.data, status.HTTP_201_CREATED)
