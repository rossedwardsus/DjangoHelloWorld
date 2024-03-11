from django.forms import ModelForm
from basic_django.models import Question

# Create the form class.
class QuestionForm(ModelForm):
     class Meta:
         model = Question
         fields = ["pub_date", "headline", "content", "reporter"]


    