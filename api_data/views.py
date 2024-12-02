from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Executive, EquityAward
from .serializers import ExecutiveSerializer, EquityAwardSerializer

@api_view(['GET'])
def getAllData(request):
    executives = Executive.objects.all()
    serializer = ExecutiveSerializer(executives, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ExecutiveSerializer(data = request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getExecutive(request, executive_id):
    executives = Executive.objects.get(pk_executive_id = executive_id)
    serializer = ExecutiveSerializer(executives)
    return Response(serializer.data)

@api_view(['GET'])
def getEquityAwardData(request, award_id):
    equity_award = EquityAward.objects.get(pk_equityaward_id = award_id)
    serializer = EquityAwardSerializer(equity_award)
    return Response(serializer.data)