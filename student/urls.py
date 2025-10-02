from django.urls import path
from .views import *

urlpatterns = [

    path('', StudentDashboardHomeView.as_view(), name='student_dashboard'),
    path("profile/create/", StudentProfileCreateView.as_view(), name="student_profile_create"),
    path('profile/', StudentProfileView.as_view(), name='student_profile'),
    path('courses/', CourseListView.as_view(), name='student_courses'),
    path('results/', ResultListView.as_view(), name='student_results'),
    path('routine/', RoutineListView.as_view(), name='student_routine'),
    path('notices/', NoticeListView.as_view(), name='student_notices'),
]
