"""scoped URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from scoped_api.views import JobView, UserView, MessageView, CrewView, GearView, ImageView, SkillsView, check_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'jobs', JobView, 'job')
router.register(r'users', UserView, 'user')
router.register(r'messages', MessageView, 'message')
router.register(r'crews', CrewView, 'crew')
router.register(r'gear', GearView, 'gear')
router.register(r'images', ImageView, 'image')
router.register(r'skills', SkillsView, 'skill')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkuser', check_user ),
    path('register', register_user),
    path('', include(router.urls))
]
