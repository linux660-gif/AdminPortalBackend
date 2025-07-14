from django.db import models

class InvestorsProfile(models.Model):
    investor_name = models.CharField(max_length = 30)
    investor_Identification_Number = models.IntegerField()
    investor_phone_number = models.IntegerField()
    investor_location = models.CharField(max_length = 40)
    investor_email = models.EmailField()
    investor_date_of_birth = models.DateField()
    #investor_total_shares = models.IntegerField()
    #investor_share_value = models.IntegerField()
   # investor_passport = models.FieldFile()