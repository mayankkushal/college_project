from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Activity, FeedbackAnswer
from details.models import Teacher, Student
from .forms import FeedbackAnswerForm
from django.forms.models import modelformset_factory


# Create your views here.
@staff_member_required
def activity_list(request):
	activity_list = Activity.objects.filter(teacher=Teacher.objects.get(user=request.user))
	return render(request, 'activity/activity_list.html', {'activity_list':activity_list})

@staff_member_required
def activity(request, pk):
	activity = Activity.objects.get(pk=pk)
	return render(request, 'activity/activity.html', {'activity':activity})

def feedback_activity(request):
	student = Student.objects.get(user=request.user)
	activity_list = Activity.objects.filter(for_class=student.student_class)
	return render(request, 'activity/feedback_activity_list.html', {'activity_list':activity_list})

def feedback(request, pk):
	activity = Activity.objects.get(pk=pk)
	student = Student.objects.get(user=request.user)
	AnswerFormSet = modelformset_factory(FeedbackAnswer, form=FeedbackAnswerForm, extra=2)
	if request.method == 'POST':
		formset = AnswerFormSet(request.POST, queryset=FeedbackAnswer.objects.none())
		if formset.is_valid():
			for form, que in zip(formset, activity.activity_type.feedback_question.all()):
				ans = form.cleaned_data.get('answer')
				print(ans)
				answer = FeedbackAnswer(answer=ans, student=student, question=que, activity=activity )
				answer.save()
		return HttpResponseRedirect(reverse('index'))
	else:
		formset = AnswerFormSet(queryset=FeedbackAnswer.objects.none())
		form_zip = zip(formset, activity.activity_type.feedback_question.all())
		return render(request, 'activity/feedback.html', {'formset':formset, 'activity':activity, 'form_zip':form_zip})

