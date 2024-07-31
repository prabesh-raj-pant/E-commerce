from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
User=get_user_model()
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    price=models.FloatField()
    discounted_price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',)
    image = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    
    def __str__(self)-> str:
        return self.name


class Customer(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    GENDER_CHOICES=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'OTHER')
    ]
    first_name=models.CharField(max_length=100,null=True)
    middle_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,null=True
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name}{self.user.email}"
    
    
    
    
    
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)

    
     
    
class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="items")

    

class Order(models.Model):
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICES,'PENDING'),
        (CONFIRM_CHOICES,'CONFIRMED'),
        (CANCEL_CHOICES,'CANCELED'),
        (COMPLETED_CHOICES,'COMPLETED')

    ]
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    status=models.CharField(max_length=2,choices=STATUS_CHOICES,default=PENDING_CHOICES)
    payment_status=models.BooleanField(default=False)
    shipping_address=models.CharField(max_length=296)

    
    
class OrderItem(models.Model):
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICES,'PENDING'),
        (CONFIRM_CHOICES,'CONFIRMED'),
        (CANCEL_CHOICES,'CANCELED'),
        (COMPLETED_CHOICES,'COMPLETED')

    ]
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=2,choices=STATUS_CHOICES,default=PENDING_CHOICES)
    order=models.ForeignKey(Order, on_delete=models.PROTECT,related_name="order_items")

    

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE) 
    star=models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )