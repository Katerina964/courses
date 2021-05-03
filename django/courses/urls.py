from django.urls import path
from courses import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/participant/<int:pk>/', views.CourseParticipantDelete.as_view())
    ]


urlpatterns = format_suffix_patterns(urlpatterns)
