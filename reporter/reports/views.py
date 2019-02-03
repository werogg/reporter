from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


# Create your views here.
class ReportViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, ]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save(reported_by=request.user.username)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
