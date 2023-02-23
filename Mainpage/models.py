from django.db import models

# Create your models here.

class ProductData(models.Model):
    product_id = models.AutoField
    product_name = models.TextField(max_length=200,default="")
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to="products")
    product_desc = models.TextField(max_length=6000,default="")
    product_cat = models.TextField(max_length=100,default="")

    def __str__(self):
        return self.product_name
    
class CartData(models.Model):
    cart_id = models.AutoField
    product_id = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.product_id) +" "+ str(self.qty)
    
class ContactForm(models.Model):
    email = models.EmailField(max_length=200,default=0)
    message = models.TextField(max_length=5000,default="")

    def __str__(self):
        return self.email
    
class OrderItem(models.Model):
    order_id = models.AutoField
    product_id = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product_id)