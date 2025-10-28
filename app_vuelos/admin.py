from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vuelo, Avion

admin.site.register(Vuelo)
admin.site.register(Avion)