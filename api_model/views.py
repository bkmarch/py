from django.template import loader
from django.http import HttpResponse

from decimal import Decimal

import requests
import json

def EquityAwardValue(request, award_id):
    response = requests.get("http://127.0.0.1:8000/api/data/getequityaward/")

    #Testing using api to get award.

    stock_price = Decimal(response.json()[0]['stockprice'])
    awards_granted = int(response.json()[0]['awardsgranted'])


    award_value = stock_price * awards_granted
    return HttpResponse(award_value)

    #return HttpResponse("The award ID is %s." % award_id)
