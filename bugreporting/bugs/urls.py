from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_report_list, name='bug_report_list'),
    path('report/<int:pk>/', views.bug_report_detail, name='bug_report_detail'),
    path('report/new/', views.bug_report_create, name='bug_report_create'),
]