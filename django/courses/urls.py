from django.urls import path, include
from courses import views
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', views.ParticipantCreateDelete)


urlpatterns = [
    path('report/<int:pk>/', views.StudentReport.as_view()),
    path('course/', views.CourseList.as_view()),
    path('', include(router.urls)),
    # path('course/participant/<int:pk>/', views.CourseParticipantDelete.as_view()),
    # path('create/', views.CourseParticipantCreate.as_view())
    ]

# urlpatterns = format_suffix_patterns(urlpatterns)
