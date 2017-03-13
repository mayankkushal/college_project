from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Activity
from details.models import Teacher


# Create your views here.
@staff_member_required
def activity_list(request):
	activity_list = Activity.objects.filter(teacher=Teacher.objects.get(user=request.user))
	return render(request, 'activity/activity_list.html', {'activity_list':activity_list})

@staff_member_required
def activity(request, pk):
	activity = Activity.objects.get(pk=pk)
	return render(request, 'activity/activity.html', {'activity':activity})