from inputs.models import Input
from inputs.serializers import InputSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def inputs_manager(request):
   if request.method == 'GET':
      input = Input.objects.all()
      serializer = InputSerializer(input, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = InputSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save(merchandise_id=request.data['merchandise'])
         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def inputs_manager_detail_and_change(request, pk):
   try:
      input = Input.objects.get(pk=pk)
   except input.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      serializer = InputSerializer(input)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = InputSerializer(input, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
