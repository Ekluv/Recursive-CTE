from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from company import utils, serializers, models
# Create your views here.


class EmployeeSubtreeApiView(APIView):

    def get(self, request, employee_id):
        response = utils.get_subtree_of_employee(employee_id)
        if not response:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.EmployeeSerializer(response)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, employee_id):
        parent_id = request.data.get('parent_id')
        if not parent_id:
            return Response({'error': 'parent_id required', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = models.Employee.objects.get(id=employee_id)
        except models.Employee.DoesNotExist:
            return Response({'error': 'invalid employee_id required', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        try:
            parent = models.Employee.objects.get(id=parent_id)
        except models.Employee.DoesNotExist:
            return Response({'error': 'invalid parent_id invalid', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        employee.parent_id = parent_id
        employee.save()

        return Response({'error':'', 'success': True}, status=status.HTTP_200_OK)



class EmployeeAncestorTreeApiView(APIView):

    def get(self, request, employee_id):
        response = utils.get_ancestor_tree(employee_id)
        if not response:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.EmployeeAncestorSerializer(response)

        return Response(serializer.data, status=status.HTTP_200_OK)



class EmployeeListSubtree(APIView):
    
    def get(self, request):
        employees = models.Employee.objects.all()
        serializer = serializers.EmployeeListSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
