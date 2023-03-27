from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls', namespace="landing")),
    path('admin/', admin.site.urls),
]
