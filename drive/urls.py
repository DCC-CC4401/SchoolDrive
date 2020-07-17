from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home_page'),
    path('logout',views.logout_user, name='logout'),
    path('profile', views.view_profile, name='profile'),
    path('files/<slug:folderid>', views.view_files, name='files'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #agregamos esta última línea