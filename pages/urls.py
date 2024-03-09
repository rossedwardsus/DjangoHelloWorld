from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("profile/<int:id>", ProfileView.as_view(), name="profile"),
    path("browse_profile", BrowseProfilesView.as_view(), name="browse_profiles"),
    path('inbox/<int:id>', inbox_view),
    path('friends_to_contact/<int:id>', friends_to_contact_view)
]