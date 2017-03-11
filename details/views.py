from django.shortcuts import render
from .models import Student, ClassDetail

# Create your views here.
def index(request):
	student_list = Student.objects.filter(student_class=ClassDetail.objects.get(sem=4, section='a')).order_by('usn')
	context_dict = {'student_list':student_list}
	return render(request, 'details/index.html', context_dict)