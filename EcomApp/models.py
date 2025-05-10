
from django.db import models


CATEGORY_CHOICES=(
    ('CR','card'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('BN','Bannana'),
    ('MG','Mango'),
    ('IC','Ice-Creme'),
    ('JI','Juice'),
)



class product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    selling_price = models.FloatField()
    diccount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title



# Product Model
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     image = models.ImageField(upload_to='products/')

#     def __str__(self):
#         return self.name



# # ✅ Product Model
# class Product(models.Model):
#     name = models.CharField(max_length=255)  # প্রোডাক্টের নাম
#     description = models.TextField(blank=True, null=True)  # বিবরণ (ঐচ্ছিক)
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # দাম
#     image = models.ImageField(upload_to='products/')  # প্রোডাক্টের ছবি
#     stock = models.PositiveIntegerField(default=0)  # স্টক সংখ্যা
#     created_at = models.DateTimeField(auto_now_add=True)  # কখন যুক্ত হয়েছে

#     def __str__(self):
#         return self.name


# # ✅ Cart Model
# class Cart(models.Model):
#     session_id = models.CharField(max_length=255, unique=True)  # সেশনের মাধ্যমে কার্ট সংরক্ষণ
#     created_at = models.DateTimeField(auto_now_add=True)  # কার্ট কখন তৈরি হয়েছে

#     def __str__(self):
#         return f"Cart {self.id}"


# # ✅ Cart Item Model (কার্টের মধ্যে কোন কোন প্রোডাক্ট আছে)
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # কোন কার্টের জন্য
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # কোন প্রোডাক্ট যোগ হয়েছে
#     quantity = models.PositiveIntegerField(default=1)  # কতগুলো প্রোডাক্ট

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"


# # ✅ Order Model
# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#     ]
    
#     name = models.CharField(max_length=255)  # কাস্টমারের নাম
#     phone = models.CharField(max_length=15)  # ফোন নম্বর
#     address = models.TextField()  # ডেলিভারি ঠিকানা
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)  # মোট মূল্য
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # অর্ডারের অবস্থা
#     created_at = models.DateTimeField(auto_now_add=True)  # কখন অর্ডার হয়েছে

#     def __str__(self):
#         return f"Order {self.id} - {self.status}"


# # ✅ Order Item Model (অর্ডারের মধ্যে কোন কোন প্রোডাক্ট আছে)
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)  # কোন অর্ডার
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # কোন প্রোডাক্ট
#     quantity = models.PositiveIntegerField(default=1)  # কতগুলো প্রোডাক্ট

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in Order {self.order.id}"



