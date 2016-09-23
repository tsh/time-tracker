from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from .models import Record
from .serializers import RecordSerializer

User = get_user_model()


class Records(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated,)
    
    
def records_view(request):
    return render_to_response('records_form.html')
