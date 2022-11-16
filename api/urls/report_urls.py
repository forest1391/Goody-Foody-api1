from django.urls import path

from api.views.tag_views import *

from api.views.report_views import get_all_reports,add_report

app_name = 'report'

urlpatterns = [
    path('all/',get_all_reports),
    path('add/',add_report),


]