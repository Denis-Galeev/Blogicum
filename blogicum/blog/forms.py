from django.contrib.auth.models import User  # type: ignore
from django.forms import DateTimeInput, ModelForm, Textarea  # type: ignore

from .models import Comment, Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'category', 'location', 'image']
        widgets = {
            'pub_date': DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea({'rows': '3'})
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
