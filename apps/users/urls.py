from django.urls import path, include
from rest_framework import routers
from .views import CreateUserView, UserListView, UserDetailView



urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='users_detail_view'),
    path('<int:pk>/', CreateUserView.as_view(), name='create_user_view'),
    path('', UserListView.as_view(), name='users_list_view'),

]