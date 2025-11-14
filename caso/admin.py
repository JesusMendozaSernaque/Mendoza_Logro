from django.contrib import admin
from .models import Promocion
from django.contrib.admin.sites import AlreadyRegistered
from .models import Caso4, CoreScale, Reglas, Rangos

class CoreScaleInline(admin.TabularInline):
    model = CoreScale
    extra = 1

class Caso4Admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'channel', 'product_code', 'valid_from', 'valid_to', 'is_scaled')
    inlines = [CoreScaleInline]

try:
    admin.site.register(Caso4, Caso4Admin)
except AlreadyRegistered:
    pass  # Evita error si ya estaba registrado

admin.site.register(CoreScale)
admin.site.register(Reglas)
admin.site.register(Promocion)
admin.site.register(Rangos)
