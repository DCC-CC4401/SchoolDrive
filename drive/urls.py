from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home_page'),
    path('logout',views.logout_user, name='logout'),
    path('profile', views.view_profile, name='profile'),
    path('files', views.view_files, name='files')
]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)