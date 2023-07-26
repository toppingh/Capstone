from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]