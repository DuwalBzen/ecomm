from django.db import models
#djanjo default user model
from django.contrib.auth.models import User
#for phone no
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    #user can have one customer and cusstomer can have one user
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone_number = PhoneNumberField(max_length=14,blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    details = models.TextField(blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Subcategory,on_delete=models.SET_NULL,null=True,blank=True)
    digital = models.BooleanField(default=False,null=True,blank=False)
    image =  models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    #if we dont have image wee get error so if image doesnt contain we return empty string
    #@property help to acccess this as attribute rather than method
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    # one customer can many order
    #if customer get delete we doesn't want to delete his order
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    #get order Total
    @property
    def get_cart_total(self):
        #we go to the product and get price
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        #we go to the product and get price
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # we can access these property in our templete
    @property
    def get_total(self):
        #we go to the product and get price
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    #we want to attach to customer and order becauser if order is deleate we still have shipting address to customer
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
