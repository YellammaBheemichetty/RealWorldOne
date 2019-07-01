from django.contrib import admin

# Register your models here.
from chat.models import Message

admin.site.register(Message)