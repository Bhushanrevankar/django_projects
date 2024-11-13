"""
URL configuration for project7 project.

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
#from atexit import register
from django.contrib import admin
from django.urls import path#, include
from courseregistration.views import register
from projecttopic.views import showproject,success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('coursereg/',register),
    path('showproject/',showproject),
    path('success/',success),
   # path('', include('courseregistration.urls')),  # Replace 'your_app' with the name of your app
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Replace with your actual view
]'''