"""
URL configuration for drf project.

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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from drfsite.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    # path(r'api/v1/auth/', include('djoser.urls')),
    # re_path(r'auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
#5d20d0f52ac5b9f8b5fd7242447c54dd94bc58b3 - test
#2871b6f6ccf8d25aaf72de5ba2571425c7ec9b95 - admin