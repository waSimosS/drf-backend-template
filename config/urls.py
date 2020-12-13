from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.auth_api.urls')),
    path('api/users/', include('apps.users.urls')),
]
