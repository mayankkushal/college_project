from django.conf.urls import url
from details import views

urlpatterns = [
	url(r'^$', views.index, name='index')
]