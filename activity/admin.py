from django.contrib import admin
from .models import ActivityType, Activity, FeedbackQuestion, FeedbackAnswer

# Register your models here.
class ActivityModel(admin.ModelAdmin):
	list_display = ('teacher_id', 'date', 'activity_type')

	def teacher_id(obj):
		return str(obj.teacher.emp_id)

	def activity_type(obj):
		return obj.activity_type.name


admin.site.register(Activity, ActivityModel)
admin.site.register(ActivityType)
admin.site.register(FeedbackQuestion)
admin.site.register(FeedbackAnswer)