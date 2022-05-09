from django.contrib import admin
from .models import Test, List, BList

# Register your models here.
admin.site.register(Test)
admin.site.register(List)
admin.site.register(BList)