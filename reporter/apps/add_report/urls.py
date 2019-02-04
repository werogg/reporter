from django.urls import path
from .views import ReportViewSet

urlpatterns = [
    path("", ReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='add_report'),
]
