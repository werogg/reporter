from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


class ReportsView(viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, ]
    queryset = Report.objects.all()
    renderer_classes = [TemplateHTMLRenderer, ]

    def get(self, request, user_id, *args, **kwargs):
        report = get_object_or_404(self.queryset, id=user_id)
        serializer = ReportSerializer(instance=report)
        return Response(serializer.data, template_name='reports/selected_report.html')

    def list(self, request, *args, **kwargs):
        try:
            searched_user = request.GET['fuser']
            queryset = Report.objects.filter(name__icontains=searched_user)
        except Exception as e:
            queryset = self.queryset
        finally:
            serializer = ReportSerializer(queryset, many=True)
            return Response({'data': serializer.data}, template_name='reports/reports_index.html')


@login_required
def new_report(self):
    return render(self, 'new_report/report.html')


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
