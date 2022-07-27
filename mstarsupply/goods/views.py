from goods.models import Merchandise
from goods.serializers import MerchandiseSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def goods_manager(request):
   if request.method == 'GET':
      merchandise = Merchandise.objects.all()
      serializer = MerchandiseSerializer(merchandise, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = MerchandiseSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def goods_manager_detail_change_and_delete(request, pk):
   try:
      merchandise = Merchandise.objects.get(pk=pk)
   except merchandise.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      serializer = MerchandiseSerializer(merchandise)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = MerchandiseSerializer(merchandise, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      merchandise.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)