# Generated by Django 3.2.23 on 2024-02-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0003_auto_20240220_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='link_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
