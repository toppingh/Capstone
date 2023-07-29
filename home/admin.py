from django.contrib import admin
from .models import *

# Register your models here.
class BlightAdmin(admin.ModelAdmin):
    list_display = ['name', 'blight_type']
    list_editable = ['name', 'blight_type']

admin.site.register(Blight, BlightAdmin)
admin.site.register(Pest)
admin.site.register(History)