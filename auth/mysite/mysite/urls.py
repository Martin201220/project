"""
URL configuration for mysite project.

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
# Import necessary modules
# from django.contrib import admin # Django admin module
# from django.urls import path	 # URL routing
# # from authentication.views import * # Import views from the authentication app
# from authentication import views
# from django.conf import settings # Application settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Static files serving

# # Define URL patterns
# urlpatterns = [
	
#     # Home page
#     path('home/', views.home, name="recipes"),      # Home page
#     path("admin/", admin.site.urls),          # Admin interface
#     path('login/', views.login, name='login.html'),    # Login page
#     path('register/', views.register, name='register.html'),  # Registration page
# ]

# # Serve media files if DEBUG is True (development mode)
# # if settings.DEBUG:
# # 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Serve static files using staticfiles_urlpatterns
# urls.py
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    # Add other URLs as needed
]
