from django.contrib import admin
from .models import Equipment
import datetime
# Register your models here.

# admin.site.site_header = "Admin Dashboard"

admin.site.site_header = "Admin Dashboard"

def issue(modeladmin, request, queryset):
    queryset.update(status='-')
    queryset.update(lastIssued=datetime.datetime.now())
    queryset.update(issued_to='CS')

issue.short_description = "Mark selected items as issued"

def ret(modeladmin, request, queryset):
    queryset.update(status='+')
    queryset.update(issued_to='')
ret.short_description = "Mark selected items as returned"


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['index', 'equip_type','actual_equipment', 'status', 'issued_to', 'lastIssued']
    list_filter = ['equip_type']
    actions = [issue, ret]


admin.site.register(Equipment, EquipmentAdmin)
# admin.site.register(Room)
