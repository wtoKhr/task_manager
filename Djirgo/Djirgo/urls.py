from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('task.urls')), если нужен фронт
    path('api/', include('api.urls')),
]