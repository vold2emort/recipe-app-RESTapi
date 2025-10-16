"""
URL for user API.
"""
from django.urls import path
from user import views

# app name gives identity to the app url can use it as reverse("user:create")
app_name = 'user'

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name='create'),
]
