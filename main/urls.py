from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScriptsViewSet, SessionsViewSet, BroadcastsViewSet, SyllabusViewSet

router = DefaultRouter()
router.register(r'scripts', ScriptsViewSet, basename='scripts')
router.register(r'sessions', SessionsViewSet, basename='sessions')  
router.register(r'broadcasts', BroadcastsViewSet, basename='broadcasts') 
router.register(r'syllabus', SyllabusViewSet, basename='syllabus') 

urlpatterns = [
    path('', include(router.urls)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
