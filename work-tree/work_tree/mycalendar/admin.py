from django.contrib import admin
from mycalendar.models import Calendar, Event
# Register your models here.
admin.site.register(Calendar)



class EventAdmin(admin.ModelAdmin):
    list_display = [ 'event_id', 'calendar_id', 'name', 'start_date', 'end_date', 'event_type']

admin.site.register(Event,EventAdmin)