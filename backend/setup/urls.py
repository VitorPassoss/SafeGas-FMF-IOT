from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
