# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Store,Order,Client,Product,Log

class ProductAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idproduct', 'name', 'manufacturer','manufacturercountry','category','type','capacity','price')

admin.site.register(Product,ProductAdmin)

class StoreAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idstore', 'name', 'adress','email')

admin.site.register(Store,StoreAdmin)

class ClientAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idclient', 'fname', 'surname','phonenumber','adress')

admin.site.register(Client,ClientAdmin)

class OrderAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idorder', 'date', 'amount','cost','product_idproduct','store_idstore','client_idclient')

admin.site.register(Order,OrderAdmin)

class LogAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id','msg', 'time')

admin.site.register(Log,LogAdmin)