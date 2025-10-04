from django.contrib import admin
from .models import MilitaryBase

class MilitaryBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'war_name', 'military_rank', 'id_number', 'phone', 'status')
    search_fields = ('name', 'war_name', 'military_rank', 'cpf', 'email')
    list_filter = ('war_name','id_number')
    ordering = ('name',)

admin.site.register(MilitaryBase, MilitaryBaseAdmin)