from django.forms import ModelForm
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            """ A placeholder and classes """
            super().__init__(*args, **kwargs)
            placeholders = {
                'subject': 'Subject',
                'reason': 'Reason for contact',
                'message': 'Message',
                'email': 'Email',
            }
            
            self.fields['email'].widget.attrs['autofocus'] = True