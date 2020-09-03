# Generated by Django 3.0.3 on 2020-09-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_premium',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volatility',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]
