from django.db import models
from datetime import datetime

class AllProduct(models.Model):
  product_name = models.CharField(max_length=20)
  category = models.CharField(max_length=20)
  weight = models.IntegerField()
  description = models.TextField(blank=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/%H/%m/%s/')
  is_published  = models.BooleanField(default=True)
  list_date = models.DateField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.product_name