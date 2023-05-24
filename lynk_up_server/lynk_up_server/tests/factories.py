import factory
from faker import Faker
from lynk_up_server.models import User, Group, Event
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = User
    abstract = False

  # user_name = fake.simple_profile()['username']
  # phone_number = fake.phone_number()
  # full_name = fake.simple_profile()['name']

  user_name = factory.LazyFunction(lambda: fake.simple_profile()['username'])
  phone_number = factory.LazyFunction(lambda: fake.phone_number())
  full_name = factory.LazyFunction(lambda: fake.simple_profile()['name'])

  id = factory.Sequence(lambda n: n + 1 )


