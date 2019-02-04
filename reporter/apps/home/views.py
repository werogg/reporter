from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from ..add_report.models import Report

#unused
@login_required
def tt(request):
    reports = Report.objects.all()

    args = {'data': reports}

    base_template_name = "home/index.html"

    return render(request, base_template_name, args)


@login_required
def by_id(request, id):
    reporte = Report.objects.get(id=id)

    return render(request, 'home/selected_report.html', {'report': reporte})


@login_required
def home(request):
    reports = Report.objects.all()

    args = {'data': reports}

    base_template_name = "home/index.html"

    user = request.GET.get('fuser', 'invalid')

    reports_to_use = []

    if user != 'invalid':
        for reporte in reports:
            if user in reporte.name:
                reports_to_use.append(reporte)
        if len(reports_to_use) == 0:
            return HttpResponseNotFound("No se ha encontrado ningún usuario")
    else:
        return render(request, base_template_name, args)

    return render(request, 'home/searched_reports.html', {'reports_to_use': reports_to_use})
