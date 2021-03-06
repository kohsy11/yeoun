"""yeoun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name = 'start'),
    path('index', views.index, name = 'index'),
    path('option', views.option, name = 'option'),
    path('common/start', views.start, name = 'start'),
    path('common/login', views.login, name = 'login'),
    path('common/registration', views.registration, name = 'registration'),
    path('com_list', views.com_list, name = 'com_list'),
    path('com_detail/<int:key>', views.com_detail, name = 'com_detail'),
    path('com_new', views.com_new, name = 'com_new'),
    path('mypage/<int:mykey>', views.mypage, name = 'mypage'),
    path('search_option', views.search_option, name = 'search_option'),
    path('search_result', views.search_result, name ="search_result"),

]
