from django.contrib import admin
from index import models
# Register your models here.
admin.site.register(models.List)
admin.site.register(models.Task)
admin.site.register(models.Contact)