from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=63)
    comment = forms.CharField(label="Your comment", max_length=255)
