from datetime import datetime
from django.shortcuts import render
from .forms import QuestionForm

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse

from basic_django.models import *

import uuid

class HomeView(TemplateView):
    template_name = "pages/home.html"

class BrowseProfilesView(TemplateView):
    template_name = "pages/browse_profiles.html"


class ProfileView(TemplateView):
    template_name = "pages/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["l"] = Article.objects.all()[:5]
        print(context)
        return context

    #def dispatch(self, request, *args, **kwargs):
    #    self.id = kwargs.get('id', "any_default")

    #@property
    #def id(self):
    #   return self.kwargs['id']


def inbox_view(request: HttpRequest, id: int):
    # write your view processing logics here
    #return HttpResponse("Welcome to Inbox")
    return render(request, "pages/inbox.html", {"id": id})


def friends_to_contact_view(request: HttpRequest, id: int):
    # write your view processing logics here
    #return HttpResponse("Welcome to Inbox")
    return render(request, "pages/friends_to_contact.html", {"id": id})

def ask_question_view(request: HttpRequest):
    # write your view processing logics here
    #return HttpResponse("Welcome to Inbox")

    form = QuestionForm(request.POST or None, request.FILES or None)

    if request.method == "GET":
        #question = Question(question_id=uuid.uuid4(), quetion_title='Refsnes', question_text, question_added_datetime=datetime.now())
        #question.save() 
        #Member.objects.all().values() 

        #context['form']= form

        return render(request, "pages/ask_question.html", {"form": form})
    elif request.method == "POST":

        q = QuestionForm(request.POST)
        q.save()

        return HttpResponse("post")


