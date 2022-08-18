from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSerializer


def people_list(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def GetUrls(request):
    return HttpResponse('Example')