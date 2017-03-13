from django.conf.urls import url
from . import views

app_name = 'activity'

urlpatterns = [
	url(r'^activity_list', views.activity_list, name='activity_list'),
	url(r'^activity/(?P<pk>[\w\-]+)', views.activity, name='activity'),
	url(r'^feedback_activity', views.feedback_activity, name='feedback_activity'),
	url(r'^feedback/(?P<pk>[\w\-]+)', views.feedback, name='feedback')
]