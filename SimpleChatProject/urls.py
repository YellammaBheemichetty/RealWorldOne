from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    re_path(r'^accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]