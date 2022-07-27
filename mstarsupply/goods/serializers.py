from dataclasses import fields
from goods.models import Merchandise

from rest_framework import serializers

class MerchandiseSerializer(serializers.ModelSerializer):
   class Meta:
      model = Merchandise
      fields = ['id', 'name', 'registration_number', 'manufacturer', 'type', 'description', 'created_at']