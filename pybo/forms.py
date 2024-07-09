from django import forms
from pybo.models import Question, Answer, Expert, Expert_answer, Pet, ForumQuestion, ForumAnswer, animal_ranking
from django.db import connection


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        connection.close()
        fields = ['subject', 'content','thumbnail']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter the Title'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder' : 'Enter the Content'
                }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'placeholder': 'Choose a file',
            }),
        }
        labels = {
            'subject': 'title',
            'content': 'content',
            'thumbnail': 'thumbnail',
        } 
        enctype = 'multipart/form-data'
    def __init__(self, *args, **kwargs):
        super(ExpertForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False
        self.fields['thumbnail'].widget.attrs.update({'class': 'custom-file-input'})



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class ExpertAnswerForm(forms.ModelForm):
    class Meta:
        model = Expert_answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['photo']

class ForumQuestionForm(forms.ModelForm):
    class Meta:
        model = ForumQuestion
        fields = ['subject', 'content', 'category']
        labels = {
            'subject': '제목',
            'content': '내용',
            
        } 
        

class ForumAnswerForm(forms.ModelForm):
    class Meta:
        model = ForumAnswer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class animalForm(forms.ModelForm):
    class Meta:
        model = animal_ranking
        connection.close()
        fields = ['subject', 'content','thumbnail']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
            'thumbnail': '썸네일',
        } 
        enctype = 'multipart/form-data'
    def __init__(self, *args, **kwargs):
        super(animalForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False


