# Generated by Django 4.2.6 on 2023-10-25 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousea',
            name='Time_Out',
        ),
    ]
