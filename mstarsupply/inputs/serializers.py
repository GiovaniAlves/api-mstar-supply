from dataclasses import fields
from inputs.models import Input
from goods.serializers import MerchandiseSerializer

from rest_framework import serializers

class InputSerializer(serializers.ModelSerializer):
   class Meta:
      model = Input
      fields = ['id', 'qtd_goods', 'date_time', 'local', 'merchandise', 'merchandise_object']
   
   merchandise = serializers.StringRelatedField(
      read_only=True,
   )
   merchandise_object = MerchandiseSerializer(
      source='merchandise',
      read_only=True,
   )