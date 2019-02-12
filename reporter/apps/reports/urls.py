from django.urls import path
from .views import ReportViewSet, ReportsView

urlpatterns = [
    # path("add", ReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='add_report'),
    # path("new", ReportsView.new_report),
    path('', ReportsView.as_view({'get': 'list'})),
    path('<int:user_id>/', ReportsView.as_view({'get': 'get'})),
]
