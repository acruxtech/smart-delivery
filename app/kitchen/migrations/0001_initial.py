# Generated by Django 5.2.4 on 2025-07-11 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'db_table': 'ingredients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('current_stock', models.FloatField(verbose_name='Доступное количество')),
                ('unit', models.CharField(help_text='шт., порц., грамм и т.д.', max_length=20, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'db_table': 'menu_items',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='kitchen.ingredient', verbose_name='Ингредиент')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='kitchen.menuitem', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'db_table': 'recipes',
            },
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredients',
            field=models.ManyToManyField(related_name='menu_items', through='kitchen.Recipe', to='kitchen.ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('menu_item', 'ingredient'), name='unique_ingredient_in_recipe'),
        ),
        migrations.AddConstraint(
            model_name='menuitem',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_menu_item_name'),
        ),
    ]
