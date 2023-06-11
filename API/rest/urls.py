from django.urls import path

from .views import PerevalAddedListView, UserListView, submit_data, update_pereval, get_data

urlpatterns = [
    path('submitData/', PerevalAddedListView.as_view()),
    path('users/', UserListView.as_view()),
    path('submitData/create/', submit_data, name='submit_data'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
    path('submitData/<int:pk>/update/', update_pereval, name='update_data'),
]

