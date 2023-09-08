from django.shortcuts import render
from .models import WorshipSchedule
from .serializers import WorshipScheduleSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


class WorshipScheduleView(generics.ListCreateAPIView):
    queryset = WorshipSchedule.objects.all()
    serializer_class = WorshipScheduleSerializer

    def get(self, request):
        try:
            worship_info = WorshipSchedule.objects.get(id=1)
        except ObjectDoesNotExist:
            worship_info = None

        if worship_info is None:
            return Response({})

        serializer = WorshipScheduleSerializer(worship_info)

        return Response(serializer.data)

    # TODO: Make secure
    @csrf_exempt
    def put(self, request):
        # Try to get the first WorshipSchedule object
        worship_info, created = WorshipSchedule.objects.update_or_create(
            id=1,
            defaults=request.data  # The fields to update
        )

        if created:
            serializer = self.serializer_class(worship_info)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = self.serializer_class(worship_info)

        return Response(serializer.data, status=status.HTTP_200_OK)
