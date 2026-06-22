from rest_framework import serializers
from .models import (Student, Course, Enrollment,Payment,Assignment,
AssignmentSubmission,CourseCompletion,Certificate)
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    # Display complete student details in response
    student = StudentSerializer(read_only=True)

    # Display complete course details in response
    course = CourseSerializer(read_only=True)

    # Accept student id while creating enrollment
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student',
        write_only=True
    )

    # Accept course id while creating enrollment
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        write_only=True
    )
    class Meta:
        model = Enrollment
        fields = ['id','student','course','student_id','course_id','enrolled_at']
    def validate(self, data):
        student = data.get('student')
        course = data.get('course')
        if Enrollment.objects.filter(
            student=student,
            course=course
        ).exists():
            raise serializers.ValidationError(
                "Student is already enrolled in this course."
            )

        return data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model = User
        fields = ['id','username','email','password']
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    def validate(self, data):
        student = data.get('student')
        course = data.get('course')
        if not Enrollment.objects.filter(
            student = student,
            course = course
        ).exists():
            raise serializers.ValidationError(
                "Student is not enrolled in this course."
            )
        if Payment.objects.filter(
            student = student,
            course = course,
            payment_status='PAID'
        ).exists():
            raise serializers.ValidationError(
                "Payment already completed for this course."
            )
        return data
    
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssignmentSubmission
        fields = '__all__'

    def validate(self, data):

        student = data.get('student')
        assignment = data.get('assignment')

        if not Enrollment.objects.filter(
            student=student,
            course=assignment.course
        ).exists():
            raise serializers.ValidationError(
                "Student is not enrolled in this course."
            )

        if AssignmentSubmission.objects.filter(
            student=student,
            assignment=assignment
        ).exists():
            raise serializers.ValidationError(
                "Assignment already submitted."
            )

        return data
    def create(self, validated_data):

        submission = super().create(validated_data)

        student = submission.student
        course = submission.assignment.course

        total_assignments = Assignment.objects.filter(
            course=course
        ).count()

        submitted_assignments = AssignmentSubmission.objects.filter(
            student=student,
            assignment__course=course
        ).count()

        completion_percentage = int(
            (submitted_assignments / total_assignments) * 100
        )

        completed = completion_percentage == 100

        CourseCompletion.objects.update_or_create(
            student=student,
            course=course,
            defaults={
                'completion_percentage': completion_percentage,
                'completed': completed
            }
        )

        return submission
    
class CourseCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCompletion
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
    def validate(self, data):
        student = data.get('student')
        course = data.get('course')

        payment_exists = Payment.objects.filter(
            student = student,
            course = course,
            payment_status = 'PAID'
            ).exists()
        if not payment_exists:
            raise serializers.ValidationError(
                "Course payment is not completed."
            )
        completion = CourseCompletion.objects.filter(
            student = student,
            course = course,
            completion_percentage=100,
            completed=True
        ).exists()
        if not completion:
            raise serializers.ValidationError(
                "Course is not completed yet."
            )
        if Certificate.objects.filter(
            student = student,
            course = course,
        ).exists():
            raise serializers.ValidationError(
                "Certificate already issued."
            )
        return data
        