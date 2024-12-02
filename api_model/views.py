from django.template import loader
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from decimal import Decimal

import requests
import json

from api_model.serializers import EquityAwardValueSerializer
from api_model.models import EquityAwardValue

@api_view(['GET'])
def getEquityAwardValue(request, award_id):
    response = requests.get("http://127.0.0.1:8000/api/data/getequityaward/%s" % award_id)

    #Testing using api to get award.

    stock_price = Decimal(response.json()['stockprice'])
    awards_granted = int(response.json()['awardsgranted'])

    
    award_value = EquityAwardValue(awardvalue = (stock_price * awards_granted))

    serializer = EquityAwardValueSerializer(award_value)
    return Response(serializer.data)
