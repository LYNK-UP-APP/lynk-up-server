from .models import User, Friend, Group, Event
from .serializers import UserSerializer, EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

