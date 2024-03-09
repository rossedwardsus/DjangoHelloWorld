from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse

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


