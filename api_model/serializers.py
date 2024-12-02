from rest_framework import serializers
from database.models import Executive, EquityAward

from api_model.models import EquityAwardValue

class ExecutiveDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

class EquityAwardDeserializer(serializers.ModelSerializer):
    class Meta:
        model = EquityAward
        fields = '__all__'
    
class EquityAwardValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquityAwardValue
        fields = '__all__'