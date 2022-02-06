#from django.contrib import admin
from django.urls import path
from . import views
app_name = 'public'
urlpatterns = [ 
    #path("admin/", admin.site.urls),

    path("", views.index, name='landing'),
    path("about", views.about, name='about'),
    path('partner_apply', views.partner_apply, name='partner_apply'),
    path('staff', views.staff, name='staff'),
    path('apply', views.apply, name='apply')
   # path("accounts/profile", views.ProfileView.as_view(), name="profile"),
 ]