from django.db import models
from django.core.files.storage import storages


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название ингредиента",
    )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ["name"]
        db_table = "ingredients"

    def __str__(self):
        return self.name


def menu_item_image_path(instance, filename):
    return f"menu_items/{instance.id}/{filename}"


class MenuItem(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название блюда",
    )
    image = models.ImageField(
        verbose_name="Фотография товара",
        upload_to=menu_item_image_path,
        storage=storages["minio"],
        blank=True,
        null=True,
        help_text="Загрузите изображение товара"
    )
    current_stock = models.FloatField(
        verbose_name="Доступное количество",
    )
    unit = models.CharField(
        max_length=20,
        verbose_name="Единица измерения",
        help_text="шт., порц., грамм и т.д."
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Recipe',
        verbose_name="Ингредиенты",
        related_name='menu_items'
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['name']
        db_table = 'menu_items'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_menu_item_name'
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.current_stock} {self.unit})"


class Recipe(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name='recipes'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ингредиент",
        related_name='recipes'
    )
    quantity = models.FloatField(
        verbose_name="Количество",
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        db_table = 'recipes'
        constraints = [
            models.UniqueConstraint(
                fields=['menu_item', 'ingredient'],
                name='unique_ingredient_in_recipe'
            )
        ]

    def __str__(self):
        return f"{self.menu_item.name} - {self.ingredient.name} ({self.quantity})"
