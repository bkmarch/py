from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Executive, EquityAward, Companies
from .serializers import ExecutiveSerializer, EquityAwardSerializer, CompaniesSerializer

from drf_spectacular.utils import extend_schema

@extend_schema(responses = ExecutiveSerializer)
@api_view(['GET'])
def getAllData(request):
    executives = Executive.objects.all()
    serializer = ExecutiveSerializer(executives, many=True)
    return Response(serializer.data)

@extend_schema(responses = ExecutiveSerializer)
@api_view(['POST'])
def addItem(request):
    serializer = ExecutiveSerializer(data = request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@extend_schema(responses = CompaniesSerializer)
@api_view(['GET'])
def getCompany(request, company_id):
    company = Companies.objects.get(pk_companies_id = company_id)
    serializer = CompaniesSerializer(company)
    return Response(serializer.data)

@extend_schema(responses = ExecutiveSerializer)
@api_view(['GET'])
def getExecutive(request, executive_id):
    executives = Executive.objects.get(pk_executive_id = executive_id)
    serializer = ExecutiveSerializer(executives)
    return Response(serializer.data)

@extend_schema(responses = EquityAwardSerializer)
@api_view(['GET'])
def getEquityAwardData(request, award_id):
    equity_award = EquityAward.objects.get(pk_equityaward_id = award_id)
    serializer = EquityAwardSerializer(equity_award)
    return Response(serializer.data)

@extend_schema(responses = CompaniesSerializer)
@api_view(['GET'])
def getCompany(request, company_id):
    company = Companies.objects.get(pk_companies_id = company_id)
    serializer = CompaniesSerializer(company)
    return Response(serializer.data)


@extend_schema(responses = CompaniesSerializer)
@api_view(['GET'])
def getCompanyEquityAwards(request, company_id):

    #companyequityawards = Companies.objects.filter(pk_companies_id = company_id)
    #serializer = CompaniesSerializer(companyequityawards, many=True)

    companyequityawards = EquityAward.objects.select_related('executive', 'executive__companies').filter(executive__companies__pk_companies_id = company_id)

    serializer = EquityAwardSerializer(companyequityawards, many=True)
    return Response(serializer.data)
