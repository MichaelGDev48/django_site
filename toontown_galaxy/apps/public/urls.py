 #from django.contrib import admin
from django.urls import path
from . import views
app_name = 'public'
urlpatterns = [ 
    #path("admin/", admin.site.urls),

    path("", views.index, name='index'),
    path("about", views.about, name="about"),
   # path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    
 ]