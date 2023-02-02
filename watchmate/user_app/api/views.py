from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .serializers import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
