from django import forms
from .models import ArticleImage, Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
		labels = {
			'name': 'Ім\'я',
			'email': 'Емейл',
			'body': 'Коментар',
		}