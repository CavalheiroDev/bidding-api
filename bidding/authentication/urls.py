from django.urls import path

from bidding.authentication.views import UserAuthAPIView, UserAuthRefreshAPIView

urlpatterns = [
    path('auth', UserAuthAPIView.as_view(), name='user-auth'),
    path('auth/refresh', UserAuthRefreshAPIView.as_view(), name='user-refresh-auth')
]
