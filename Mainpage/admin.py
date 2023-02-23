from django.contrib import admin
from .models import ProductData,CartData,ContactForm,OrderItem
# Register your models here.

admin.site.register(ProductData)
admin.site.register(CartData)
admin.site.register(ContactForm)
admin.site.register(OrderItem)