# Generated by Django 2.0.6 on 2018-06-07 01:30

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
