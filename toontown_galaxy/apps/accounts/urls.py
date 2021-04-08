from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'accounts'
urlpatterns = [  
  path("profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path(
        "login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path('register', auth_views.LoginView.as_view(template_name="accounts/register.html"), name='register'),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),

]