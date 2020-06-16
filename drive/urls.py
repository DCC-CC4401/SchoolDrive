from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('logout',views.logout_user, name='logout'),
    path('profile', views.view_profile, name='profile'),
    path('files', views.view_files, name='files')
]