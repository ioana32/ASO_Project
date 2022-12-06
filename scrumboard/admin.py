from django.contrib import admin

from scrumboard.models import Message, Room

admin.site.register(Room)
admin.site.register(Message)
