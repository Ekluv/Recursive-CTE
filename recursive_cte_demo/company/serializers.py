from rest_framework import serializers

from company.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee

EmployeeSerializer._declared_fields['sub_emp'] = EmployeeSerializer(many=True)


class EmployeeAncestorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        

EmployeeAncestorSerializer._declared_fields['parents'] = EmployeeAncestorSerializer(many=True)



class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee