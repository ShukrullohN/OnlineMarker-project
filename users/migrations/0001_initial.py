# Generated by Django 5.0.6 on 2024-06-15 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='full_name')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='company')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='city')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='phone')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='VerificationCodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_codes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Verification Code',
                'verbose_name_plural': 'Verification Codes',
            },
        ),
    ]
