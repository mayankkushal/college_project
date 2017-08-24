from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Activity, FeedbackAnswer, FeedbackQuestion
from details.models import Teacher, Student
from .forms import FeedbackAnswerForm, ActivityForm
from django.forms.models import modelformset_factory

import csv


# Create your views here.
@staff_member_required
def activity_list(request):
	activity_list = Activity.objects.filter(teacher=Teacher.objects.get(user=request.user))
	return render(request, 'activity/activity_list.html', {'activity_list':activity_list})


@staff_member_required
def activity(request, pk):
	activity = Activity.objects.get(pk=pk)

	#getting all the different answer counts
	total_answers = FeedbackAnswer.objects.filter(activity=activity).count()
	low_no = FeedbackAnswer.objects.filter(activity=activity, answer="Low").count()
	medium_no = FeedbackAnswer.objects.filter(activity=activity, answer="Medium").count()
	high_no = FeedbackAnswer.objects.filter(activity=activity, answer="High").count()

	context_dict = {'activity':activity, "low_no":low_no, "total_answers":total_answers,
					 "medium_no":medium_no, "high_no":high_no}
	return render(request, 'activity/activity.html', context_dict)


def feedback_activity(request):
	student = Student.objects.get(user=request.user)
	activity_list = Activity.objects.filter(attendance=student)
	return render(request, 'activity/feedback_activity_list.html', {'activity_list':activity_list})


def feedback(request, pk):
	activity = Activity.objects.get(pk=pk)
	student = Student.objects.get(user=request.user)

	feedback = False
	answer = FeedbackAnswer.objects.filter(student=student, activity=activity)
	if answer:
		feedback = True
		return render(request, 'activity/feedback.html', {'feedback':feedback,'activity':activity})
	else:
		question_count = FeedbackQuestion.objects.all().count()
		AnswerFormSet = modelformset_factory(FeedbackAnswer, form=FeedbackAnswerForm, extra=question_count)
		if request.method == 'POST':
			formset = AnswerFormSet(request.POST, queryset=FeedbackAnswer.objects.none())
			if formset.is_valid():
				for form, que in zip(formset, FeedbackQuestion.objects.all()):
					ans = form.cleaned_data.get('answer')
					answer = FeedbackAnswer(answer=ans, student=student, question=que, activity=activity)
					answer.save()
			return HttpResponseRedirect(reverse('activity:feedback_activity'))
		else:
			formset = AnswerFormSet(queryset=FeedbackAnswer.objects.none())
			form_zip = zip(formset, FeedbackQuestion.objects.all())
			return render(request, 'activity/feedback.html', {'formset':formset, 'activity':activity, 'form_zip':form_zip})


@staff_member_required
def activity_entry(request):
	if request.method == 'POST':
		activity_form = ActivityForm(request.POST)
		if activity_form.is_valid():
			activity = activity_form.save(commit=False)
			activity.teacher = Teacher.objects.get(user=request.user)
			activity.save()
			return HttpResponseRedirect(reverse('activity:activity_list'))
		else:
			return HttpResponse("Entry Failed. Try again")
	else:
		activity_form = ActivityForm()
		return render(request, 'activity/activity_entry.html', {'activity_form':activity_form})


def download_csv(request, pk):
	"""
		Renders all the emails of the `Newsletter` to a .csv file.
		Only admin is allowed to download.
	"""
	if request.user.is_superuser:
		activity = Activity.objects.get(pk=pk)
		student_list = Student.objects.filter(activity=activity)

		response =  HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment;filename='+activity.topic+'.csv'

		writer = csv.writer(response)
		writer.writerow(['USN', 1,2,3,4,5,6,7,8,9,10,11,12])
		for st in student_list:
			row = [st.usn]
			feedback = FeedbackAnswer.objects.filter(student=st, activity=activity)
			for f in feedback:
				row.append(f.answer)
			writer.writerow(row)

		return response
	else:
		return redirect(reverse('index'))
 