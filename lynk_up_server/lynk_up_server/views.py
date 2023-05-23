from .models import User, Friend, Group, Event
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

@api_view(['GET'])
def user_list(request):

  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"data": serializer.data})


@api_view(['GET'])
def user_detail(request, phone_number):
  try:
    user = User.objects.get(phone_number=phone_number)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = UserSerializer(user)
    return Response({"data": serializer.data})

@api_view(['GET'])
def group_list(request):

  if request.method == 'GET':
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response({"data": serializer.data})

@api_view(['GET'])
def group_detail(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)

@api_view(['GET'])
def event_list(request):
  if request.method == 'GET':
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({"data": serializer.data})

@api_view(['GET'])
def event_detail(request, event_id):
  try:
    event = Event.objects.get(pk=event_id)
  except Event.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = EventSerializer(event)
    return Response({"data": serializer.data})

@api_view(['POST'])
def add_friend(request, user_id):
  try:
    user = User.objects.get(id=request.data['user_id'])
    friend = User.objects.get(id=request.data['friend_id'])

    if friend not in user.added_friends():
      Friend.objects.create(user=user, friend=friend)

  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  except Friend.IntegrityError:
    return Response(status=status.HTTP_409_CONFLICT)

  serializer = FriendsListSerializer(user.added_friends(), many=True)
  return Response(
    {"data": {"friends":serializer.data}}, status=201, content_type='application/json'
  )
