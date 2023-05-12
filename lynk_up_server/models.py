from django.db import models

class User(models.Model):
  user_name = models.CharField()
  phone_number = models.CharField(max_length=12)
  full_name = models.CharField()
