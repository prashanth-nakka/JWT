from django.urls import path
from account import views
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]
