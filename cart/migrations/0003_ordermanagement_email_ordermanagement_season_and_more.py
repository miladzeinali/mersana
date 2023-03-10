# Generated by Django 4.1.7 on 2023-03-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_mobile_ordermanagement_extramobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermanagement',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordermanagement',
            name='season',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ordermanagement',
            name='extramobile',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
