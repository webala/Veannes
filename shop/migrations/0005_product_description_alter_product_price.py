# Generated by Django 4.0.3 on 2022-03-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
