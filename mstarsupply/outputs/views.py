from outputs.models import Output
from inputs.models import Input
from outputs.serializers import OutputSerializer
from inputs.serializers import InputSerializer
from django.db.models import Sum

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def outputs_manager(request):

   if request.method == 'GET':
      outputs = Output.objects.all()
      serializer = OutputSerializer(outputs, many=True)
      return Response(serializer.data)

   elif request.method == 'POST':
      # verificando a disponibilidade da mercadoria
      inputs = Input.objects.filter(merchandise_id=request.data['merchandise']).aggregate(Sum('qtd_goods'))
      outputs = Output.objects.filter(merchandise_id=request.data['merchandise']).aggregate(Sum('qtd_goods'))
      
      # Se não tiver valor nenhum assume o valor zero '0'
      stock = (inputs['qtd_goods__sum'] or 0) - (outputs['qtd_goods__sum'] or 0)

      if request.data['qtd_goods'] <= stock:
         serializer = OutputSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save(merchandise_id=request.data['merchandise'])
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(f"No momento possuímos apenas {stock} unidade(s) dessa mercadoria!", status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT'])
def outputs_manager_detail_and_change(request, pk):
   try:
      output = Output.objects.get(pk=pk)
   except input.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      serializer = OutputSerializer(output)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = OutputSerializer(output, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def outputs_by_month(request, month):
   try:
      output = Output.objects.filter(date_time__month=month)
   except output.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   serializer = OutputSerializer(output, many=True)
   return Response(serializer.data)

