# Generated by Django 4.0.2 on 2022-03-07 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_owner'),
        ('accounts', '0002_remove_vendor_shop_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]