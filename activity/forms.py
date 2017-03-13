from django import forms
from .models import FeedbackAnswer

class FeedbackAnswerForm(forms.ModelForm):
	choices = FeedbackAnswer.CHOICES

	answer = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())
	class Meta:
		model = FeedbackAnswer
		fields = ('answer', )