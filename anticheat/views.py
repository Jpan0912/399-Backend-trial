from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSerializer



#Example code
def people_list(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return JsonResponse(serializer.data, safe=False)

#Webscraping code
@api_view(['GET'])
def GetUrls(request):
    """


    :param request:  - which would be your filename

    :code - followed by your webscraping code
    :return: - can workout the response variable but potentially a Json Object containing information such as what site and the respective URL.
    """


    return HttpResponse('Example')