from django.contrib import admin

# Register your models here.
from administrativo.models import Provincia

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capital', 'población')

admin.site.register(Provincia, ProvinciaAdmin)