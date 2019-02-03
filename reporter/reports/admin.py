from django.contrib import admin

from .models import Report


# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', 'reported_by')
    fields = ('name', 'reported_by', 'timestamp', 'reason')

    class Meta:
        model = Report
