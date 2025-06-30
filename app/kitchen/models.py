from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    current_stock = models.FloatField()
    min_stock = models.FloatField()


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='Recipe')


class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
