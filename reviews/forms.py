from django.forms import ModelForm, Textarea
from reviews.models import Review

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['rating', 'comment']
		widgets = {
			'comment' : Textarea(attrs={'rows':15, 'cols':40})
		}