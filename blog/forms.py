from django import forms
from .models import Aritcle


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	phone = forms.CharField(max_length=11)
	comments = forms.CharField(required=False, widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Aritcle
		fields = ['title', 'subtitle', 'content']
		labels = {'title': '1', 'subtitle': '', 'content': ''}
		widgets = {'content': forms.Textarea(attrs={'cols': 80})}
