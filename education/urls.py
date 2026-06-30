from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    StudentViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    PaymentViewSet,
    AssignmentViewSet,
    AssignmentSubmissionViewSet,
    CourseCompletionViewSet,
    CertificateViewSet,
    UserRegistrationView,
    DashboardStatsView,


)

router = DefaultRouter()

router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('enrollments', EnrollmentViewSet)
router.register('payments',PaymentViewSet)
router.register('assignments',AssignmentViewSet)
router.register('assignment-submission',AssignmentSubmissionViewSet)
router.register('course-completions',CourseCompletionViewSet)
router.register('certificates',CertificateViewSet)
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('dashboard-stats/',DashboardStatsView.as_view(),name='dashboard-stats'),
]

urlpatterns += router.urls