# Generated by Django 3.2.8 on 2021-10-29 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marineapp', '0013_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
