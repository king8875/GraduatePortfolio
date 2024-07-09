from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserProfileView

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('landing/', views.landing, name='landing'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),

]
