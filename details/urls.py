from django.conf.urls import url
from details import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^account/registration/student_register', views.student_register, name='student_register')
]