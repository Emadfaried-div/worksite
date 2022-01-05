from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
from .models import CheckList, UtilityCheckList, MaintenancePlan


admin.site.register(CheckList)
admin.site.register(UtilityCheckList)


class MaintenancePlanAdmin(ImportExportActionModelAdmin):
    list_display =['calendar_name', 'event_name', 'jan', 'feb', 'mar', 'apr', 'may', 'jun','jul','aug','sep','oct','nov','dec']
    search_fields = ['calendar_name', 'event_name', 'jan', 'feb', 'mar', 'apr', 'may', 'jun','jul','aug','sep','oct','nov','dec']
    
admin.site.register(MaintenancePlan,MaintenancePlanAdmin)