from django import forms
from .models import Message, Comment, Like


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__' #['content']
