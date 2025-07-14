from django.contrib import admin

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ingredient, MenuItem, Recipe


class RecipeInline(admin.TabularInline):
    """Встроенная форма для редактирования ингредиентов блюда"""
    model = Recipe
    extra = 1  # Количество пустых форм для добавления
    verbose_name = "Ингредиент в рецепте"
    verbose_name_plural = "Ингредиенты в рецепте"
    fields = ('ingredient', 'quantity')  # Поля для отображения



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Админка для ингредиентов"""
    list_display = ('name',)  # Отображаемые поля в списке
    search_fields = ('name',)  # Поля для поиска
    ordering = ('name',)  # Сортировка
    list_per_page = 20  # Пагинация


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Админка для пунктов меню"""
    list_display = ('name', 'current_stock', 'unit')  # Поля в списке
    list_editable = ('current_stock', 'unit')  # Редактируемые поля в списке
    search_fields = ('name',)  # Поиск по названию
    list_filter = ('unit',)  # Фильтры справа
    inlines = [RecipeInline]  # Встроенная форма рецептов
    fieldsets = (
        (None, {
            'fields': ('name', 'current_stock', 'unit', 'image', 'image_preview')
        }),
    )
    ordering = ('name',)
    list_per_page = 20
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;"/>')
        return "Нет изображения"
    image_preview.short_description = "Превью"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Админка для рецептов (отдельно)"""
    list_display = ('menu_item', 'ingredient', 'quantity')
    list_filter = ('menu_item', 'ingredient')
    search_fields = ('menu_item__name', 'ingredient__name')
    raw_id_fields = ('menu_item', 'ingredient')  # Для удобства при большом количестве
    ordering = ('menu_item', 'ingredient')
    list_per_page = 30
