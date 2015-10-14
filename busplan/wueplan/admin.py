from django.contrib import admin
from .models import Station, Lines, Times

admin.site.register(Station)
admin.site.register(Lines)
admin.site.register(Times)
# Register your models here.
