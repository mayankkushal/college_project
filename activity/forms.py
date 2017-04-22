from django import forms
import datetime
from .models import FeedbackAnswer, Activity


class HorizontalRadioSelect(forms.RadioSelect):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		css_style = 'style="display: inline-block; margin-right: 10px;"'

		self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'

class FeedbackAnswerForm(forms.ModelForm):
	choices = FeedbackAnswer.CHOICES

	answer = forms.ChoiceField(choices=choices, widget=HorizontalRadioSelect(), label="")
	class Meta:
		model = FeedbackAnswer
		fields = ('answer', )

class ActivityForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Activity
		fields = ('__all__')
