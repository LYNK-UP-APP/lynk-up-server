# import pytest
# from django.urls import reverse
# from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
# from lynk_up_server.models import User, Group, Friend


# @pytest.mark.django_db
# def test_group_detail(client):
#     # create a sample user
#     user = User.objects.create(user_name="test_user", phone_number="1234567890", full_name="Test User")

#     # create a sample group for the user
#     group = Group.objects.create(user=user, name="Test Group")

#     # test valid group id
#     response = client.get(reverse('group_detail', kwargs={'group_id': group.id}))
#     assert response.status_code == HTTP_200_OK
#     assert response.data['name'] == 'Test Group'

#     # test invalid group id
#     response = client.get(reverse('group_detail', kwargs={'group_id': 9999}))
#     assert response.status_code == HTTP_404_NOT_FOUND
