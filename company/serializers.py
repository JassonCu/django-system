from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'legal_business_name', 'nit', 'is_dummy', 'is_active']


class CompanyNitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('nit', )

class CompanyDPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('dpi',)