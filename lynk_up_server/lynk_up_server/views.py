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
def user_detail(request, user_id):
  try:
    user = User.objects.get(pk=user_id)
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

@api_view(['POST'])
def group_create(request):
  serializer = GroupSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def group_update(request, group_id):
  try:
    group = Group.objects.get(pk=group_id)
  except Group.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'PUT':
    serializer = GroupSerializer(group, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
def group_delete(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def event_list(request):
  if request.method == 'GET':
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({"data": serializer.data})
<<<<<<< HEAD
  
  if request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
=======

@api_view(['GET'])
>>>>>>> main
def event_detail(request, event_id):
  try:
    event = Event.objects.get(pk=event_id)
  except Event.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = EventSerializer(event)
    return Response({"data": serializer.data})
<<<<<<< HEAD
  
  elif request.method == 'PUT':
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
=======

@api_view(['POST'])
def add_friend(request, user_id):
  try:
    user = User.objects.get(id=request.data['user_id'])
    friend = User.objects.get(id=request.data['friend_id'])

    if friend not in user.added_friends():
      Friend.objects.create(user=user, friend=friend)

  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  except IntegrityError:
    return Response(status=status.HTTP_409_CONFLICT)

  serializer = FriendsListSerializer(user.added_friends(), many=True)
  return Response(
    {"data": {"friends":serializer.data}}, status=201, content_type='application/json'
  )
>>>>>>> main
