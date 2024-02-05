from django.contrib import admin
from .models import Newsletter

# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """ Sign up to newsletter """ 
    list_display = (
        'email',
        'name',
    )
