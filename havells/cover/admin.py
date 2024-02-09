from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'created_at', 'updated_at', 'is_active', 'category', 'image')