from django.db import models
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()


class Billing(models.Model):
    products = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Customer(models.Model):
    total_bill = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
