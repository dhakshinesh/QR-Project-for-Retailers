# Generated by Django 3.1.3 on 2020-11-24 16:20

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_productinfo_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='company',
            field=models.CharField(max_length=30, null=True, verbose_name=django.db.models.fields.CharField),
        ),
    ]