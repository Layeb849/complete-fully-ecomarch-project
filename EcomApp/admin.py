from django.contrib import admin
from .models import  Cart, Product,Order,OrderItem




admin.site.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']
    
admin.site.register(Cart)    
admin.site.register(Order)    
admin.site.register(OrderItem)    