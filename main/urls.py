from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScriptsViewSet, SessionsViewSet, BroadcastsViewSet, SyllabusViewSet, TrainerViewSet , ApplyViewSet, ContactViewSet, SubscribeViewSet

router = DefaultRouter()
router.register(r'apply', ApplyViewSet, basename='apply')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'subscribe', SubscribeViewSet, basename='subscribe')
router.register(r'scripts', ScriptsViewSet, basename='scripts')
router.register(r'sessions', SessionsViewSet, basename='sessions')  
router.register(r'broadcasts', BroadcastsViewSet, basename='broadcasts') 
router.register(r'syllabus', SyllabusViewSet, basename='syllabus') 
router.register(r'trainers', TrainerViewSet, basename='trainers')

urlpatterns = [
    path('', include(router.urls)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
