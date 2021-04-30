from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('courses.urls')),
    path('admin/', admin.site.urls),
]
