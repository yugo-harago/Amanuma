from rest_framework import generics
from .models import UsefulLink
from .serializers import UsefulLinkSerializer

class UsefulLinkListCreateView(generics.ListCreateAPIView):
    queryset = UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer
