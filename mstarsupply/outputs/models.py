from django.db import models
from goods.models import Merchandise

class Output(models.Model):
   qtd_goods = models.IntegerField()
   date_time = models.DateTimeField(auto_now_add=True)
   local = models.CharField(max_length=120)
   type = models.CharField(max_length=120, default='output')
   merchandise = models.ForeignKey(Merchandise, related_name='outputs', on_delete=models.CASCADE)
