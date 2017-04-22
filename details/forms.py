from django import forms
from .models import Student, ClassDetail
from django.contrib.auth.models import User

class StudentRegisterForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('student_class', 'usn', 'join_year')