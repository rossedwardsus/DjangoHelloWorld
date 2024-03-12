from django.forms import ModelForm
from django import forms
from basic_django.models import Question, User

# Create the form class.
class QuestionForm(ModelForm):
     class Meta:
        model = Question
        #fields = ["pub_date", "headline", "content", "reporter"]
        fields = ["question_category", "question_title", "question_text"]


        STREET_NAME_CHOICES = (
            ('Car Accident', 'Car Accident'), 
            ('Streetname2', 'Street name 2')
        )
            
        #question_cateogry = forms.ChoiceField(
        #    widget=forms.Select,
        #    choices=STREET_NAME_CHOICES
        #)

        widgets = {
            'question_category': forms.Select(choices=STREET_NAME_CHOICES),
        }

class UserForm(ModelForm):
     class Meta:
        model = User
        #fields = ["pub_date", "headline", "content", "reporter"]
        fields = ["first_name", "last_name", "user_type", "about_me"]


        STREET_NAME_CHOICES = (
            ('lawyer', 'Lawyer'), 
            ('Ive been in this situaiton Before', 'Street name 2')
        )
            
        #question_cateogry = forms.ChoiceField(
        #    widget=forms.Select,
        #    choices=STREET_NAME_CHOICES
        #)

        widgets = {
            'user_type': forms.Select(choices=STREET_NAME_CHOICES),
        }

