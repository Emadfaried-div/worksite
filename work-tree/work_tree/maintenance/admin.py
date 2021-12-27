from django.contrib import admin

# Register your models here.
from .models import CheckList, UtilityCheckList


admin.site.register(CheckList)
admin.site.register(UtilityCheckList)