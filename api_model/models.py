from django.db import models


class EquityAwardValue(models.Model):
    #this calculated value data model will be part of Scorecard data model.
    executivename = models.CharField(max_length = 200)
    awardvalue = models.DecimalField(max_digits = 18, decimal_places=2)

