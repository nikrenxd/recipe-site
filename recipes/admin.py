from django.contrib import admin

from .models import Recipe, Ingredient, Instruction
from comments.models import Comment


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 0


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created", "updated"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    inlines = [IngredientInline, InstructionInline, CommentInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Instruction)
class Instruction(admin.ModelAdmin):
    pass
