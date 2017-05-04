from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Student, ClassDetail
from .forms import StudentRegisterForm


# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'details/index.html', context_dict)

def student_register(request):
	if request.method == 'POST':
		student_form = StudentRegisterForm(request.POST)
		if student_form.is_valid():
			student = student_form.save(commit=False)
			student.user = request.user
			student.save()
			return HttpResponseRedirect(reverse('activity:feedback_activity'))
		else:
			return HttpResponse("Registration Failed. Try again")
	else:
		student_form = StudentRegisterForm()
		return render(request, 'details/student_register.html', {'student_form':student_form})

from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(self, request, user):
		return HttpResponseRedirect(reverse('student_register'))