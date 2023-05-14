# Although this is called a view in django, this "API view" actually functions more similarly
# to a rails controller.

from django.http import JsonResponse

def api_home(request, *args, **kwargs):
  return JsonResponse({"message": "Hi there, this is your Django API response!!!"})
