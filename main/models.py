from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class ProductInfo(models.Model):
    index = models.AutoField(primary_key=True)
    name = models.CharField(CharField, max_length=200 )
    price = models.IntegerField(IntegerField)
    status = models.CharField(CharField, max_length=8)
    location = models.CharField(CharField, blank=True, null=True, max_length=20)
    timestamp = models.DateTimeField(blank=True, null=True)
    key = models.CharField(CharField, max_length=16)

    class Meta:
        managed = True
        db_table = 'main_productinfo'
