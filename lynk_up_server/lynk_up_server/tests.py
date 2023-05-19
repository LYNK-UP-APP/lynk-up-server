from django.test import TestCase
from lynk_up_server.models import User

class UserTestCase(TestCase):
  def test_setup(self):
    User.objects.create(user_name='TesseracT', phone_number='927-298-1029', full_name='Antonio King Hunt')
    User.objects.create(user_name='TesseracT', phone_number='927-298-1029', full_name='Antonio King Hunt')

  def has_attributes(self):
    tesseract = User.objects.get(User.user_name)
