from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=500)
	hod = models.CharField(max_length=125)
	no_of_teachers = models.PositiveIntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Branches'

class ClassDetail(models.Model):
	branch = models.ForeignKey(Branch, related_name="branch", null=True)
	sem = models.CharField(max_length=5)
	section = models.CharField(max_length=5)
	no_of_stu = models.PositiveIntegerField()
	year = models.PositiveIntegerField()

	def __str__(self):
		return str(self.year)+"-"+self.sem+"-"+self.section


class Student(models.Model):
	user = models.OneToOneField(User, related_name="student_detail")
	student_class = models.ForeignKey(ClassDetail, related_name="student_class")
	usn = models.CharField(max_length=15, unique=True)
	join_year = models.PositiveIntegerField()

	def __str__(self):
		return self.usn

class Teacher(models.Model):
	user = models.OneToOneField(User, related_name="teacher_details")
	emp_id = models.CharField(max_length=20, unique=True)
	join_year = models.PositiveIntegerField(null=True)
	no_of_subs = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.emp_id


