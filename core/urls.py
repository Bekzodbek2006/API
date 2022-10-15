from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
    # path("registration/", include("registration_api.urls"))
]
