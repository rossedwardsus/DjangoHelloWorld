from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("profile/<int:id>", ProfileView.as_view(), name="profile"),
    path("browse_profile", BrowseProfilesView.as_view(), name="browse_profiles"),
    path('inbox/<int:id>', inbox_view),
    path('friends_to_contact/<int:id>', friends_to_contact_view),
    path('ask_question', ask_question_view),
    path('browse_questions', browse_questions_view),
    path('view_legal_question', view_legal_question_view),
    path('edit_profile', edit_profile_view),
    path('user_home', user_home_view)
]