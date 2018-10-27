from django.contrib import admin
from .models import Raza,Estado,Mascota

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'descripcion')
    search_fields = ['nombre','raza']
    list_filter = ('raza',)


admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota, MascotaAdmin)