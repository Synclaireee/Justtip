from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/', include('testEndPoint.urls')),
    path('r/', include('regtest.urls')),
]
