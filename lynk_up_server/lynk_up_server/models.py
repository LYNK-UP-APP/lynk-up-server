# for a pre-authenticated user model
from django.contrib.auth.models import models
# from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
  user_name = models.CharField(max_length=20, unique=True)
  phone_number = models.CharField(max_length=12, unique=True)
  full_name = models.CharField(max_length=40)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user_name


class FriendList(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
  friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.user_name

  def add_friend(self, account):
    if not account in self.friends.all():
      self.friends.add(account)
      self.save

class Group(models.Model):
  friends = models.ManyToManyField(FriendList)
  name = models.CharField(max_length=40)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Event(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  date = models.CharField(max_length=50)
  time = models.CharField(max_length=40)
  address = models.CharField(max_length=60)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
