from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=20 , verbose_name="First Name" , null=True , blank=True)
    last_name = models.CharField(max_length=20 , verbose_name="Last Name" , null=True , blank=True)
    email = models.EmailField(max_length=100 , verbose_name="Email" , null=True , blank=True)
    phone = models.CharField(max_length=13 , verbose_name="Phone Number" , unique=True ,
                             error_messages={"unique":"This phone number is already registered"})
    password = models.CharField(max_length=8,verbose_name="Password")
    password_repeat = models.CharField(max_length=8,verbose_name="Repeat Password")
    wish_list = models.ManyToManyField("Product", verbose_name="Wish List", blank=True,
                                       related_name="users_wish_list")
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='hexashop_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='hexashop_user_permissions',
        blank=True
    )

class Category(models.Model):
    slug = models.SlugField(max_length=100 , verbose_name="Slug" , null=True , blank=True)
    name = models.CharField(max_length=100 , unique=True , verbose_name="Category Name")

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100 , unique=True , verbose_name="Type Name")
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , verbose_name="Category")

    def __str__(self):
        return self.name

class Product(models.Model):
    slug = models.SlugField(max_length=100 , unique=True , verbose_name="Slug")
    name = models.CharField(max_length=100 , verbose_name="Product Name")
    description = models.CharField(max_length=1000 , verbose_name="Description")
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , verbose_name="Category")
    price = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name = "Price")
    brand = models.CharField(max_length=100 , verbose_name = "Brand")
    color = models.CharField(max_length=100 , verbose_name = "Color")
    discount = models.PositiveSmallIntegerField(default=0 , verbose_name="Discount",help_text='discount %')
    type = models.ForeignKey(Type , on_delete=models.SET_NULL , null=True , verbose_name="Type")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name="Product",related_name="images")
    image = models.ImageField(upload_to='product/image/' , verbose_name="Product Image")

    def __str__(self):
        return str(self.product.pk)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser , on_delete=models.SET_NULL , null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.created)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.PROTECT)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

