from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view, profile_view, edit_profile_view
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='accounts/password_change.html', success_url='/accounts/profile/'), name='password_change'),
]