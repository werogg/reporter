from django.conf.urls import url
from django.urls import path
from .views import ReportViewSet, ReportsView

urlpatterns = [
    path("add", ReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='add_report'),
    path("new", ReportsView.new_report),
    url(r'^$', ReportsView.reports),
    url(r'^(?P<id>\d+)/$', ReportsView.by_id),
]
