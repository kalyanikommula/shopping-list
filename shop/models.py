from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

COUNTY_CHOICES = (
    ('Bedfordshire', 'Bedfordshire'),
    ('Berkshire', 'Berkshire'),
    ('Buckinghamshire', 'Buckinghamshire'),
    ('Berwickshire', 'Berwickshire'),
    ('cheshire', 'cheshire'),
    ('cornwall', 'cornwall'),
    ('Dovan', 'Dovan'),
    ('Dorset', 'Dorset'),
    ('Hampshire', 'Hampshire'),
    ('Kent', 'Kent'),
    ('Yorkshire', 'Yorkshire'),
    )

CATEGORY_CHOICES = (
    ('CU', 'Curd'),
    ('ML', 'Milk'),
    ('BU', 'Butter'),
    ('MS', 'Milkshake'),
    ('PN', 'Panner'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-creams'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = CloudinaryField('product', default='placeholder')

# product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    postcode = models.CharField(max_length=200)
    county = models.CharField(choices=COUNTY_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product_discounted_price


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
