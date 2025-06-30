from django.db import models


class Order(models.Model):
    STATUSES = [('new', 'New'), ('preparing', 'Preparing'), ('delivering', 'Delivering')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_zone = models.CharField(max_length=100)
    items = models.ManyToManyField('MenuItem', through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderGroup(models.Model):
    orders = models.ManyToManyField(Order)
    delivery_zone = models.CharField(max_length=100)
    preparation_start_time = models.DateTimeField()
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
