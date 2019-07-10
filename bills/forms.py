from django import forms


class PostForm(forms.Form):
	cover = forms.ImageField() 
	title = forms.CharField()
