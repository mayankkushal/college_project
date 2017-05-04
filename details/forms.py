from django import forms
from .models import Student, ClassDetail
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class StudentRegisterForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('student_class', 'usn', 'join_year')
		labels = {
            'student_class': _('You are in Class'),
            'join_year': _('You joined in the year')
        }