from django.urls import path

from profiles.views import *

urlpatterns = [
    path('create-profile/', create_profile, name="create-profile"),
    path('get-profile-all/', get_profile_all, name="get-profile-all"),
    path('get-profile/<int:id>', get_profile, name="get-profile"),
    path('create_url/<int:profile_id>', create_url, name="create_url"),
    path('get_url_all/<int:profile_id>', get_url_all, name="get_url_all")
]