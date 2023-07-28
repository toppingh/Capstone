from django.contrib import admin
from .models import Blight, Pest, History

# Register your models here.
admin.site.register(Blight)
admin.site.register(Pest)
admin.site.register(History)