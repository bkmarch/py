from rest_framework import serializers
from database.models import Executive, EquityAward

from api_model.models import EquityAwardValue
    
class EquityAwardValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquityAwardValue
        fields = '__all__'
