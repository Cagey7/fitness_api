# Generated by Django 5.0.2 on 2024-04-07 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_client_height_client_trainers_client_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(250)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='weight',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(300)]),
        ),
    ]