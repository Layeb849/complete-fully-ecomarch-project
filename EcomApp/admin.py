from django.contrib import admin
from .models import  product




admin.site.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']