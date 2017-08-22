from django.db import models
from details.models import Teacher, Student, ClassDetail
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class ActivityType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=5000)
	other_details = models.TextField(max_length=5000)

	def __str__(self):
		return self.name


class Activity(models.Model):
	activity_type = models.ForeignKey(ActivityType, related_name="activity", null=True)
	teacher = models.ForeignKey(Teacher, related_name="activity")
	for_class = models.ForeignKey(ClassDetail, related_name='class_activity')
	date = models.DateField(null=True)
	topic = models.CharField(max_length=200)
	description = models.TextField(max_length=5000)
	resource = models.TextField(max_length=5000)
	attendance = models.ManyToManyField(Student, help_text='Hold down "Control", or "Command" on a Mac, to select more than one.')

	def __str__(self):
		return self.topic
	
	def get_absolute_url(self):
		return '/activity/activity/%s'% self.pk

	class Meta:
		verbose_name_plural = "Activities"

class FeedbackQuestion(models.Model):
	question = models.TextField(max_length=5000)

	def __str__(self):
		return self.question

class FeedbackAnswer(models.Model):
	activity = models.ForeignKey(Activity, related_name="feedback_ans", null=True)
	student = models.ForeignKey(Student)
	question = models.ForeignKey(FeedbackQuestion)
	CHOICES = [('Low','Low'), ('Medium','Medium'), ('High','High')]
	answer = models.CharField(max_length=50, choices=CHOICES, default='Please Stop')

	def __str__(self):
		return self.student.usn



