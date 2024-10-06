# Generated by Django 3.2.25 on 2024-09-02 09:41
# flake8: noqa
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240902_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='noimage', max_length=255, null=True, verbose_name='image'),
        ),
    ]
