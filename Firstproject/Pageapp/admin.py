from django.contrib import admin
from .models import Laptop

# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','ram','rom','price','processor','document']
admin.site.register(Laptop,LaptopAdmin)


