from django.template import loader
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers

from decimal import Decimal

import requests, json

from api_model.serializers import EquityAwardValueSerializer
from api_model.models import EquityAwardValue

from database.models import Executive, EquityAward


@api_view(['GET'])
def getEquityAwardValue(request, award_id):
    response = requests.get("http://127.0.0.1:8000/api/data/equityaward/%s" % award_id)

    #Testing using api to get award.
    executivename = response.json()['executive']['executivename']
    stock_price = Decimal(response.json()['stockprice'])
    awards_granted = int(response.json()['awardsgranted'])
    award_value = EquityAwardValue(awardvalue = (stock_price * awards_granted), executivename = executivename)
    serializer = EquityAwardValueSerializer(award_value)

    return Response(serializer.data)

@api_view(['GET'])
def getCompanyEquityAwards(request, company_id):
    response = requests.get("http://127.0.0.1:8000/api/data/company/%s/equityawards" % company_id)

    serializer_list = []

    for js in response.json():

        stock_price = Decimal(js['stockprice'])
        awards_granted = int(js['awardsgranted'])
        award_value_instance = EquityAwardValue(awardvalue = stock_price * awards_granted)
        serializer_list.append(award_value_instance)
        
    serializer = EquityAwardValueSerializer(serializer_list, many=True)

    return Response(serializer.data)