# Generated by Django 4.1.7 on 2023-03-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_product_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
