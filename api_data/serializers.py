from rest_framework import serializers
from database.models import Companies, Executive, EquityAward


class CompaniesSerializer(serializers.ModelSerializer):

    #executive = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Companies
        fields = '__all__'

class ExecutiveSerializer(serializers.ModelSerializer):

    companies = CompaniesSerializer()
    #equityaward = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Executive
        fields = '__all__'

class EquityAwardSerializer(serializers.ModelSerializer):

    executive = ExecutiveSerializer()
    #executive = ExecutiveSerializer()

    class Meta:
        model = EquityAward
        fields = '__all__'
    