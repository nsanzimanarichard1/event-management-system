from django.contrib import admin

# Register your models here.
from .models import Event,Category,Schedule
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Schedule)