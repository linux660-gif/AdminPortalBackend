from rest_framework import serializers
from .models import InvestorsProfile


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorsProfile
        fields = '__all__'
        
