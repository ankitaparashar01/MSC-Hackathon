# Generated by Django 3.2.8 on 2021-11-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marineapp', '0003_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='download.png', null=True, upload_to='media'),
        ),
    ]
