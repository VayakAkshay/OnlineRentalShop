from django.contrib import admin
from .models import ProductData,CartData,ContactForm,OrderItem

class ProductDataAdmin(admin.ModelAdmin):
    list_display = ["product_name","product_price","product_desc","product_cat"]

class CartDataAdmin(admin.ModelAdmin):
    list_display = ["product_id","qty","user_id"]

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["email","message"]

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ["product_id","qty","user_id"]

admin.site.register(ProductData,ProductDataAdmin)
admin.site.register(CartData,CartDataAdmin)
admin.site.register(ContactForm,ContactFormAdmin)
admin.site.register(OrderItem,OrderItemsAdmin)