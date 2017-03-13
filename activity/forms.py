from django import forms
from .models import FeedbackAnswer

class FeedbackAnswerForm(forms.ModelForms):
	class Meta:
		model = FeedbackAnswer
		fields = ('answer')