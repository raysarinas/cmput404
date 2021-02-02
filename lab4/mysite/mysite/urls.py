"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

# this is the MYSITE/MYSITE urls.py

# http://127.0.0.1:8000/??????? <-- this file decides wheremsdt it goes

urlpatterns = [
    path('polls/', include('polls.urls')), # anything that starts with http://127.0.0.1:8000/polls/ will be handled further by polls/urls.py
    path('admin/', admin.site.urls),
]
