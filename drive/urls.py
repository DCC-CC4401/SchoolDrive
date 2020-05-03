from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('register', views.register_user, name='register_user'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
]