from django.urls import path

from users.views import UserUpdateAPIView, UserRetrieveAPIView, SubscriptionToggleAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('profile/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('subscribe/', SubscriptionToggleAPIView.as_view(), name='subscription_toggle')
]
