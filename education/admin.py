from django.contrib import admin
from .models import (Student, Course, Enrollment,Payment,Assignment,
AssignmentSubmission,CourseCompletion,Certificate)

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone')
    search_fields = ('name','email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_name','duration','fee')
    search_fields = ['course_name']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id','student','course','enrolled_at')
    list_filter = ('course','enrolled_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','student','course','amount','payment_status','transaction_id','payment_date')
    list_filter = ('transaction_id','student__name')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=('id','title','course','due_date','total_marks')
    search_fields=('title','course__course_name')
    list_filter=('course','due_date')

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id','student','assignment','marks_obtained','submitted_at')    
    search_fields = ('student__name','assignment__title')
    list_filter = ('submitted_at',)

@admin.register(CourseCompletion)
class CourseCompletionAdmin(admin.ModelAdmin):
    list_display = ('id','student','course','completion_percentage','completed')
    list_filter = ('completed',)
    search_fields = ('student__name','course__course_name')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','certificate_number','student','course','issued_at')
    search_fields = ('certificate_number','student__name','course__course_name')
    list_filter = ('issued_at',)   


