from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        labels = {
            "subject" : "제목",
            "content" : "내용",
        }
        widgets = {
            "subject" : forms.TextInput(attrs={"class" : "form-control"}),
            "content" : forms.Textarea(attrs={"class" : "form-control", "rows" : 10}),
        }