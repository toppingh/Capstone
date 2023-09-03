from django.urls import path, include
from .views import UserProfileAPIView, ChangeUsername, get_csrf_token, ChangeProfileImg

app_name = 'accounts'

urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('profile/', UserProfileAPIView.as_view(), name='change'),
    path('change/profile/', ChangeProfileImg.as_view(), name='profile'),
    path('change/username/', ChangeUsername.as_view(), name='change_username'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]