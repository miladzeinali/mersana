# Generated by Django 3.1 on 2023-03-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_ordermanagement_sended'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermanagement',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
