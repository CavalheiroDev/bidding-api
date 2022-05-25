from django.urls import path

from bidding.user.views import UserCreateAPIView

urlpatterns = [
    path('user', UserCreateAPIView.as_view(), name='user-create'),
]
