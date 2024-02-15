from .models import Comments
from django import forms

class CreateCommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='',
                                   widget=forms.Textarea(
                                       attrs={'class': 'form-control',
                                              'placeholder': "Введите текст комментария"}))

    class Meta:
        model = Comments
        fields = ('comment_text', )