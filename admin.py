from django.contrib import admin
from tryapp.models import *


@admin.register(ProductMainModel)
class ProductMainModelAdmin(admin.ModelAdmin):
    list_display = ['id','titles','description','price','unique_code','size','mainchoice']

@admin.register(ProductColourModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['id','chice_color']

@admin.register(ProductImageModel)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id','product','image']