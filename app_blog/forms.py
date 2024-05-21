from django import forms
from .models import ArticleImage, Comment


class ArticleImageForm(forms.ModelForm):
	# image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	image = forms.ImageField(widget=forms.ClearableFileInput())
	# image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	# image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
	# image = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)

	class Meta:
		model = ArticleImage
		fields = '__all__'


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')