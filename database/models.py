# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EquityAward(models.Model):
    pk_equityaward_id = models.AutoField(db_column='PK_EquityAward_Id', primary_key=True)  # Field name made lowercase.
    awardtype = models.CharField(db_column='AwardType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    awardsgranted = models.IntegerField(db_column='AwardsGranted', blank=True, null=True)  # Field name made lowercase.
    grantdate = models.DateField(db_column='GrantDate', blank=True, null=True)  # Field name made lowercase.
    stockprice = models.DecimalField(db_column='StockPrice', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    executive = models.ForeignKey('Executive', models.DO_NOTHING)

    class Meta:
        db_table = 'EquityAward'


class Executive(models.Model):
    executivename = models.CharField(db_column='ExecutiveName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    executivetitle = models.CharField(db_column='ExecutiveTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pk_executive_id = models.AutoField(db_column='PK_Executive_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Executive'

