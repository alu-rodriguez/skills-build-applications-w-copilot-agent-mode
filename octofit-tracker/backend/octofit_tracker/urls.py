"""octofit_tracker URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import os
from .views import (
    api_root,
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet
)

# Get Codespace name from environment variable
CODESPACE_NAME = os.getenv('CODESPACE_NAME')

# Create router with custom root URL if in Codespaces
class CustomDefaultRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        api_root_dict = {}
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework.reverse import reverse
        
        class APIRoot(APIView):
            def get(self, request, *args, **kwargs):
                ret = {}
                namespace = request.resolver_match.namespace
                for key, url_name in api_root_dict.items():
                    if namespace:
                        url_name = namespace + ':' + url_name
                    try:
                        ret[key] = reverse(
                            url_name,
                            args=args,
                            kwargs=kwargs,
                            request=request,
                            format=kwargs.get('format')
                        )
                    except:
                        ret[key] = None
                
                # Update URLs to use CODESPACE_NAME if available
                if CODESPACE_NAME:
                    for key in ret:
                        if ret[key]:
                            ret[key] = ret[key].replace('http://', 'https://')
                            if 'localhost' in ret[key] or '127.0.0.1' in ret[key]:
                                ret[key] = f'https://{CODESPACE_NAME}-8000.app.github.dev/api/{key}/'
                
                return Response(ret)
        
        return APIRoot.as_view()

router = CustomDefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
