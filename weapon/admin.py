from django.contrib import admin
from .models import Weapon

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('type', 'model_type', 'serial_number', 'caliber', 'manufacturer', 'owner', 'status')
    search_fields = ('type', 'model_type', 'serial_number', 'caliber', 'manufacturer', 'owner__name', 'status')
    list_filter = ('type', 'model_type', 'caliber', 'status')
    ordering = ('type',)

admin.site.register(Weapon, WeaponAdmin)

