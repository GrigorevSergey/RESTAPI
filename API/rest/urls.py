from django.urls import path

from .views import PerevalAddedListView, UserListView

urlpatterns = [
    path('submitData/', PerevalAddedListView.as_view()),
    path('users/', UserListView.as_view()),
]

