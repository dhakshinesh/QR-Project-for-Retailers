# Generated by Django 3.1.3 on 2020-11-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201123_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinfo',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='productinfo',
            table='ProdctInfo',
        ),
    ]
