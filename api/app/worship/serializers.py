from rest_framework import serializers
from .models import WorshipSchedule


class WorshipScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorshipSchedule
        fields = ('info', )
