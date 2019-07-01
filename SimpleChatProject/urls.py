from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
]


