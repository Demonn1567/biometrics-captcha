"""
URL configuration for biometrics project.

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
from django.urls import path
from userbehavior.views import UserBehaviorView, GetUser, GetSingleUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/behavior/', UserBehaviorView.as_view(), name = 'user_behavior'),
    path('api/behavior/generic', GetUser.as_view()),
    path('api/behavior/generic/<int:id>',GetSingleUser.as_view())
    
]
