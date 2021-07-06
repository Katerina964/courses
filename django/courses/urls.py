from django.urls import path
from courses import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'courses'
urlpatterns = [
    path('report/<int:pk>/', views.StudentReport.as_view(), name='report'),
    path('api/course/', views.CourseList.as_view(), name='list'),
    path('participant/<int:pk>/', views.ParticipantDelete.as_view(), name='delete'),
    path('create/', views.ParticipantCreate.as_view(), name='create')
    ]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'csv'])
