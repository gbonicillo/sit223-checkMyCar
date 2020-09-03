from django.contrib import admin
from .models import Make, Issue, Car

# Register your models here.

admin.site.register(Issue)
admin.site.register(Car)
admin.site.register(Make)