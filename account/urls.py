from django.urls import path
from account import views
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', views.UserChangePasswordView.as_view(),
         name='change_password'),
    path('send-reset-password-email/',
         views.SendPasswordEmailView.as_view(), name='reset-password-email'),
    path('reset-password/<uid>/<token>/',
         views.UserPasswordResetView.as_view(), name='reset-password'),
]
