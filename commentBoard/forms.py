from django import forms

class postForm(forms.Form):
	user = forms.CharField(label='Username', max_length=128)
	content = forms.CharField(label='Post', max_length=400 ,  widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))

class commentForm(forms.Form):
	user = forms.CharField(label='Username', max_length=128)
	content = forms.CharField(label='Comment', max_length=400,  widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
