from django.db import models
from django.contrib.auth.models import User
from .consts import gender_field
import uuid


class Course(models.Model):
    course=models.CharField(max_length=20,blank=False)
    branch=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return f'{self.course} {self.branch}'

class Subject(models.Model):
    # course=models.CharField(max_length=20,choices=course_field,blank=True)
    # branch=models.CharField(max_length=50,choices=branch_field,blank=True)
    # subject_name=models.CharField(max_length=75)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    subject_full_name=models.CharField(max_length=60,blank=False)
    subject_short_name=models.CharField(max_length=15,blank=False)
    subject_code=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return f'{self.subject_full_name}'


class Teacher(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    first_name=models.CharField(max_length=40,blank=False)
    last_name=models.CharField(max_length=40,blank=False)
    mobile_number = models.CharField(max_length=15, blank=False,unique=True, help_text='Enter your mobile number')

    email = models.EmailField(unique=True, help_text='Enter your email address')

    password = models.CharField(max_length=128, help_text='Enter your password',blank=False)
    gender=models.CharField(max_length=10,choices=gender_field,blank=False)
    date_of_birth=models.DateField()
   
    address=models.CharField(max_length=100,blank=False)
    image_teacher=models.ImageField(upload_to='teachers/', null=True, blank=True)
    # branch_course=models.CharField(max_length=20,blank=True)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserDetail(models.Model):
    first_name=models.CharField(max_length=30,blank=False)
    last_name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(unique=True,blank=False)
    password=models.CharField(max_length=40,blank=False)
    confirm_password=models.CharField(max_length=40,blank=False,help_text="Enter above passord Correctly")
    phone_number=models.CharField(max_length=10,blank=False,help_text="Enter Phone Number")
    roll_number=models.CharField(max_length=20,blank=False,help_text='Enter Permanent Roll Number')
    course=models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
#     # branch_course=models.CharField(max_length=20,choices=branch_course_field,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Subject(models.Model):
    # course=models.CharField(max_length=20,choices=course_field,blank=True)
    # branch=models.CharField(max_length=50,choices=branch_field,blank=True)
    # subject_name=models.CharField(max_length=75)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    subject_full_name=models.CharField(max_length=60,blank=False)
    subject_short_name=models.CharField(max_length=15,blank=False)
    subject_code=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return f'{self.subject_full_name}'


  
class Assignment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    assignment_title=models.CharField(max_length=30,blank=False)
    assignment_description=models.TextField(max_length=200,blank=False)
    submission_last_date=models.DateField()
    # course=models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    assignment_marks=models.CharField(max_length=10,blank=False)
    assignment_file=models.FileField(upload_to='assignment/', null=True, blank=True)

    def __str__(self):
        return f'{self.assignment_title}'

class New(models.Model):
    title=models.CharField(max_length=30,blank=False)
    description=models.TextField(max_length=350,blank=False)

    def __str__(self):
        return f'{self.title}'


class Upload(models.Model):
    assignment_description=models.CharField(max_length=200,blank=False)
    upload_assignment=models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f'{self.description}'

class NewsByTeacher(models.Model):
    news_title=models.CharField(max_length=30,blank=False)
    news_description=models.TextField(max_length=200,blank=False)
    

    def __str__(self):
        return f'{self.news_title}'