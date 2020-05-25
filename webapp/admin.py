from django.contrib import admin
from .models import employees, package

# Register your models here.
admin.site.register(employees)
admin.site.register(package)