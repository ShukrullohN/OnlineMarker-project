# Generated by Django 5.0.4 on 2024-06-14 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productbrandmodel',
            options={'verbose_name': 'Product Brand', 'verbose_name_plural': 'Product Brands'},
        ),
    ]