# Generated by Django 3.1.1 on 2020-09-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200903_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]