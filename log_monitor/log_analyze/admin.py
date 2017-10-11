from django.contrib import admin
from .models import LogMonitor

# Register your models here.
# class LogMonitorAdmin(admin.ModelAdmin):
# 	pass
admin.site.register(LogMonitor)
