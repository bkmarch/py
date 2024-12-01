from rest_framework import serializers
from database.models import Executive, EquityAward

class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

class EquityAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquityAward
        fields = '__all__'
    