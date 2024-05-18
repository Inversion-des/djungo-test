from django import forms
from .models import ArticleImage


class ArticleImageForm(forms.ModelForm):
	# image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	image = forms.ImageField(widget=forms.ClearableFileInput())
	# image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	# image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
	# image = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)


	class Meta:
		model = ArticleImage
		fields = '__all__'