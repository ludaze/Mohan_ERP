from django.db import models

# Create your models here.
class FGRN(models.Model):
    FGRN_no = models.TextField(primary_key= True)
    recieved_from = models.TextField(blank=True, null= True)
    recieved_by = models.TextField(blank=True, null= True)
    date = models.DateField()

class FGRN_item(models.Model):
    FGRN_no = models.ForeignKey('FGRN', on_delete=models.CASCADE,db_column = 'FGRN_no')
    item_id = models.AutoField(primary_key= True)
    item_name = models.TextField(blank=True, null= True)
    quantity = quantity = models.FloatField()
    remarks = models.TextField(blank=True, null= True)

class finished_goods(models.Model):
    item_name = models.TextField(primary_key=True)
    quantity = quantity = models.FloatField()