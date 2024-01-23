from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True)


class Type(BaseModel):
    name = models.CharField(max_length=56)


class Feature(BaseModel):
    name = models.CharField(max_length=56)


class Product(BaseModel):
    name = models.CharField(max_length=56)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField()
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.CharField(max_length=56)
    model = models.CharField(max_length=56)
    feature_id = models.ManyToManyField(Feature, related_name='products')
    description = models.TextField()


class ProductImage(BaseModel):
    image = models.ImageField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact_us(BaseModel):
    ContactChoise = [
        ("buy", 'Buy'),
        ('sell', 'Sell'),
        ('promotion', 'Promotion'),
        ('order', 'Order'),
    ]

    name = models.CharField(max_length=56)
    number = PhoneNumberField(region='UZ')
    reason = models.CharField(max_length=56, choices=ContactChoise)
    subject = models.TextField()

    def get_absolute_url(self):
        return reverse('shop:contact-page',)

class About(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=56)
    description = models.TextField()
