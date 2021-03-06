# Generated by Django 3.1.3 on 2020-11-22 18:06

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name=django.db.models.fields.CharField)),
                ('price', models.IntegerField(verbose_name=django.db.models.fields.IntegerField)),
                ('status', models.CharField(max_length=8, verbose_name=django.db.models.fields.CharField)),
                ('location', models.CharField(blank=True, max_length=20, null=True, verbose_name=django.db.models.fields.CharField)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=16, verbose_name=django.db.models.fields.CharField)),
            ],
            options={
                'db_table': 'product_details',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
