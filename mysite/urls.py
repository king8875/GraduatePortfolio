
from django.contrib import admin
from django.urls import path, include, re_path
from pybo import views
from rest_framework import routers
from pybo.views import MovieViewSet
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter() 
router.register('movies',MovieViewSet) # prefix = movies , viewset = MovieViewSet

urlpatterns = [
    path("pybo/", include('pybo.urls')),
    #path('pybo/', include('allauth.urls')),
    path('pybo/',include('django.contrib.auth.urls')),
    #path('accounts/',include('django.contrib.auth.urls')),
    #path('accounts/',include('allauth.urls')),
    #re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/',include(router.urls)),
    path("admin/", admin.site.urls),
    
    path('common/', include('common.urls')),
    path('', views.main, name='main'),  # '/' 에 해당되는 path
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
