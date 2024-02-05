from django.contrib import admin
from .models import Post, Comment, Category
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """ Posts for blogs posted """ 
    list_display = (
        'title',
        'slug',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
