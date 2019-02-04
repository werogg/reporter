from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('name', 'reported_by','punish', 'timestamp', 'reason',)
        read_only_fields = ('reported_by', 'timestamp')
