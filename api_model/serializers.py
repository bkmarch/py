from rest_framework import serializers
from database.models import Executive, EquityAward

class ExecutiveDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

class EquityAwardDeserializer(serializers.ModelSerializer):
    class Meta:
        model = EquityAward
        fields = '__all__'
    