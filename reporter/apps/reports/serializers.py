from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True, format='%d-%m-%Y')

    class Meta:
        model = Report
        fields = ('id', 'name', 'reported_by', 'punish', 'timestamp', 'reason')
        read_only_fields = ('id', 'reported_by', 'timestamp')
