from django.urls import path, include

from .views import UserProfileAPIView, get_csrf_token, ChangeProfileImg, validate_jwt_token, send_email, check_auth_code

app_name = 'accounts'

urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='get_profile'),
    path('change/profile/<int:pk>/', ChangeProfileImg.as_view(), name='profile'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('token/', validate_jwt_token, name='jwt_token'),
    path('send_email/', send_email, name='send_email'),
    path('check_auth_code/', check_auth_code, name='check_auth_code'),
]