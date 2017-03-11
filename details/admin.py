from django.contrib import admin
from .models import ClassDetail
from .models import Student
from .models import Teacher, Branch


# Register your models here.
admin.site.register(ClassDetail)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Branch)