from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (Student, Course, Enrollment,Payment,Assignment,
AssignmentSubmission,CourseCompletion,Certificate)
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    PaymentSerializer,
    AssignmentSerializer,
    AssignmentSubmissionSerializer,
    CourseCompletionSerializer,
    CertificateSerializer
)
from .permissions import IsAdminOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    search_fields = ['name', 'email']
    filterset_fields = ['name']
    ordering_fields = ['name', 'id']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

    search_fields = ['course_name']
    filterset_fields = ['course_name']
    ordering_fields = ['fee', 'duration']


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['student', 'course']

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    search_fields = ['title']
    filter_fields = ['course']
    ordering_fields = ['due_date','total_marks']

class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer

    filterset_fields = ['student','assignment']
    ordering_fields = ['submitted_at','marks_obtained']

class CourseCompletionViewSet(viewsets.ModelViewSet):
        queryset = CourseCompletion.objects.all()
        serializer_class = CourseCompletionSerializer

        filterset_fields = ['student','course','completed']

class CertificateViewSet(viewsets.ModelViewSet):
     queryset = Certificate.objects.all()
     serializer_class = CertificateSerializer
     filterset_fields = ['student','course']

class DashboardStatsView(APIView):
     def get(self,request):
          data = {
               "courses":Course.objects.count(),
               "assignments":Assignment.objects.count(),
               "payments":Payment.objects.count(),
               "certificates":Certificate.objects.count(),
          }
          return Response(data)