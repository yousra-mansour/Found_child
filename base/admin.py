from django.contrib import admin
from .models import found_child_data,missing_child_data

admin.site.register(found_child_data)
admin.site.register(missing_child_data)