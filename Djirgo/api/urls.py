from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import TaskViewSet


router = SimpleRouter()

router.register('tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
