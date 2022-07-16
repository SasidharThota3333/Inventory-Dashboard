from django.contrib import admin
from .models import *
# Register your models here.

#For changing admin page header
admin.site.site_header = 'Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter= ['category']

admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','staff','order_quantity','date')
    list_filter= ['staff']

admin.site.register(Order,OrderAdmin)