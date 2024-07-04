from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend_app.views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'items', ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
