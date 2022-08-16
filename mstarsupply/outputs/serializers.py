from dataclasses import fields
from outputs.models import Output
from goods.serializers import MerchandiseSerializer

from rest_framework import serializers

class OutputSerializer(serializers.ModelSerializer):
   class Meta:
      model = Output
      fields = ['id', 'qtd_goods', 'date_time', 'local', 'type', 'merchandise', 'merchandise_object']
   
   merchandise = serializers.StringRelatedField(
      read_only=True,
   )
   merchandise_object = MerchandiseSerializer(
      source='merchandise',
      read_only=True,
   )