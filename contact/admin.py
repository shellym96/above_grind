from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Contact filters on admin panel """

    list_display = ('email', 'subject', 'message', 'reason')
    search_fields = ('email', 'reason')
    list_filter = ('email', 'reason')
    