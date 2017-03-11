from django.contrib import admin
from .models import ActivityType, Activity, FeedbackQuestion, FeedbackAnswer

# Register your models here.

admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(FeedbackQuestion)
admin.site.register(FeedbackAnswer)