from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


class ReportsView:
    @login_required
    def by_id(self, req_id):
        db_reports = Report.objects.get(id=req_id)

        return render(self, 'reports/selected_report.html', {'report': db_reports})

    @login_required
    def reports(self):
        db_reports = Report.objects.all()

        args = {'data': db_reports}

        base_template_name = "reports/reports_index.html"

        user = self.GET.get('fuser', 'invalid')

        reports_to_use = []

        if user != 'invalid':
            for reporte in db_reports:
                if user in reporte.name:
                    reports_to_use.append(reporte)
            if len(reports_to_use) == 0:
                return HttpResponseNotFound("No se ha encontrado ningún usuario")
        else:
            return render(self, base_template_name, args)

        return render(self, 'reports/searched_reports.html',
                      {'reports_to_use': reports_to_use})

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
