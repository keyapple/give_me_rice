from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_diaply_links = (
    )

    search_fields = (
        'title',
    )
    
    list_filter = (
        'user',
    )

    list_display = (
        'title',
        'id',
        'image',
        'content',
        'user',
        'view_count',
        'created_at',
        'updated_at',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'id',
        'user',
        'post',
        'created_at',
        'updated_at',
    )

@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'ingredient',
        'id',
        'created_at',
        'updated_at',
    )



@admin.register(models.Postingre)
class PostingreAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',
        'ingredient',
        'ingredient_id',
        'quantity',
        'id',
        'created_at',
        'updated_at',
    )