from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
    # path("registration/", include("registration_api.urls")),
    # path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
