from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"
    
class Payment(models.Model):

    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed')
    ]

    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='payments')
    course = models.ForeignKey( Course, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField( max_digits=10,decimal_places=2)
    payment_status = models.CharField( max_length=20, choices=PAYMENT_STATUS,default='PENDING')
    transaction_id = models.CharField(max_length=100,unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"

class Assignment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='assignments')
    title=models.CharField(max_length=200)
    description=models.TextField()
    due_date=models.DateField()
    total_marks=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='submissions')
    submission_url = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    marks_obtained = models.PositiveIntegerField(null=True,blank=True)
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"

class CourseCompletion(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='course_completions')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_completions')
    completion_percentage=models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"
    
class Certificate(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='certificates')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='certificates')
    certificate_number = models.CharField(max_length=50,unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate_number