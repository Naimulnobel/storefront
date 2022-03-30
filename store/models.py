from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    Membership_Bronze = 'B'
    Membership_Silver = 'S'
    Membership_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (Membership_Bronze, 'Bronze'),
        (Membership_Silver, 'Silver'),
        (Membership_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=Membership_Bronze)


class Order(models.Model):
    STATUS = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=STATUS, default='P')


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
