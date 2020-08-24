from django.urls import path, include
from . import views as base_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('', base_views.base, name='base' ),
    # path('signup/', base_views.signup, name='signup'),
    path('blog/', base_views.secret_page, name='blog'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', base_views.registerPage, name='register'),
    path('login', base_views.loginPage, name='login'),
    path('logout', base_views.logoutUser, name='logout'),
    path('change_password/', base_views.change_password, name='change_password'),
]