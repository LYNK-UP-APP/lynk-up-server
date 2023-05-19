import pytest
from lynk_up_server.models import User, FriendsList, Group, Event

def test_user_creation():
    user = User.objects.create(user_name='bobz', phone_number='123-456-7890', full_name='Bob Bobberton')
    assert user.phone_number == '123-456-7890'
    assert user.full_name == 'User 1'