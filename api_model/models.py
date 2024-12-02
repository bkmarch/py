from django.db import models


class EquityAwardValue(models.Model):
    awardvalue = models.DecimalField(max_digits = 18, decimal_places=2)

