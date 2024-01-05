"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route
from rest_framework.authtoken.views import obtain_auth_token

from dj_rest_auth.views import LogoutView  # Import the built-in LogoutView

# from .views import logout_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Use the built-in LogoutView
    path('dj-rest-auth/logout/', LogoutView.as_view(), name='rest_logout'),
    # path('api/dj-rest-auth/logout/', logout_route),
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token login endpoint
    path('api-auth/', include('rest_framework.urls')), #Adds the login

    path('api/', include('fishes.urls')),
    # path('api/', include('like.urls')),
]
