from django.db import models

class User(models.Model):
  user_name = models.CharField(max_length=20, unique=True)
  phone_number = models.CharField(max_length=12, unique=True)
  full_name = models.CharField(max_length=40)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user_name


class Friend(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  friend_id = models.IntegerField()

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
  friends = models.ManyToManyField(Friend)
  name = models.CharField(max_length=40)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

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
