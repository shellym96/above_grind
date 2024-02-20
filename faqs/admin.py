from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'link_text',
        'link_url',
    )

admin.site.register(FAQ, FAQAdmin)
