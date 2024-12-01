from django.template import loader
from django.http import HttpResponse

from .models import Executive

from decimal import Decimal

import requests
import json

def index(request):

    exec_names_recent = Executive.objects.all()
    output = ", ".join([e.ExecutiveName for e in exec_names_recent])
    return HttpResponse(output)


def ExecutiveTest(request, executive_id):
    return HttpResponse("The executive ID is %s." % executive_id)

def EquityAwardValue(request, award_id):
    response = requests.get("http://127.0.0.1:8000/api/data/getequityaward/")

    #Testing using api to get award.

    stock_price = Decimal(response.json()[0]['StockPrice'])
    awards_granted = int(response.json()[0]['AwardsGranted'])


    award_value = stock_price * awards_granted
    return HttpResponse(award_value)

    #return HttpResponse("The award ID is %s." % award_id)

