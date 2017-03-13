from django.contrib import admin
from .models import ClassDetail
from .models import Student
from .models import Teacher, Branch


# Register your models here.     			
class StudentModel(admin.ModelAdmin):
	list_display = ('usn', 'student_name', 'student_class')

	def student_name(self, obj):
		return obj.user.username

class TeacherModel(admin.ModelAdmin):
	list_display = ('employee_id', 'employee_name')

	def employee_id(self, obj):
		return obj.emp_id

	def employee_name(self, obj):
		return obj.user.username


admin.site.register(ClassDetail)
admin.site.register(Student, StudentModel)
admin.site.register(Teacher, TeacherModel)
admin.site.register(Branch)