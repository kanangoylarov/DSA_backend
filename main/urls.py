<<<<<<< HEAD
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
=======
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_view, name='apply_form'),
    path('contact/', views.contact_view, name='contact_form'),
    path('subscribe/', views.subscribe_view, name='subscribe_form'),
    path('success/', views.success_view, name='success'),
]



##urls for Scripts--------------------------------------------------------------------------------------------------


from django.urls import path
from .views import (
    ScriptsListView, ScriptsDetailView, ScriptsCreateView, ScriptsUpdateView, ScriptsDeleteView,
    SessionsListView, SessionsDetailView, SessionsCreateView, SessionsUpdateView, SessionsDeleteView,
    BroadcastsListView, BroadcastsDetailView, BroadcastsCreateView, BroadcastsUpdateView, BroadcastsDeleteView,
    SyllabusListView, SyllabusDetailView, SyllabusCreateView, SyllabusUpdateView, SyllabusDeleteView
)

urlpatterns = [
    # Scripts
    path('scripts/', ScriptsListView.as_view(), name='scripts_list'),
    path('scripts/<int:pk>/', ScriptsDetailView.as_view(), name='scripts_detail'),
    path('scripts/create/', ScriptsCreateView.as_view(), name='scripts_create'),
    path('scripts/update/<int:pk>/', ScriptsUpdateView.as_view(), name='scripts_update'),
    path('scripts/delete/<int:pk>/', ScriptsDeleteView.as_view(), name='scripts_delete'),

    # Sessions
    path('sessions/', SessionsListView.as_view(), name='sessions_list'),
    path('sessions/<int:pk>/', SessionsDetailView.as_view(), name='sessions_detail'),
    path('sessions/create/', SessionsCreateView.as_view(), name='sessions_create'),
    path('sessions/update/<int:pk>/', SessionsUpdateView.as_view(), name='sessions_update'),
    path('sessions/delete/<int:pk>/', SessionsDeleteView.as_view(), name='sessions_delete'),

    # Broadcasts
    path('broadcasts/', BroadcastsListView.as_view(), name='broadcasts_list'),
    path('broadcasts/<int:pk>/', BroadcastsDetailView.as_view(), name='broadcasts_detail'),
    path('broadcasts/create/', BroadcastsCreateView.as_view(), name='broadcasts_create'),
    path('broadcasts/update/<int:pk>/', BroadcastsUpdateView.as_view(), name='broadcasts_update'),
    path('broadcasts/delete/<int:pk>/', BroadcastsDeleteView.as_view(), name='broadcasts_delete'),

    # Syllabus
    path('syllabus/', SyllabusListView.as_view(), name='syllabus_list'),
    path('syllabus/<int:pk>/', SyllabusDetailView.as_view(), name='syllabus_detail'),
    path('syllabus/create/', SyllabusCreateView.as_view(), name='syllabus_create'),
    path('syllabus/update/<int:pk>/', SyllabusUpdateView.as_view(), name='syllabus_update'),
    path('syllabus/delete/<int:pk>/', SyllabusDeleteView.as_view(), name='syllabus_delete'),
]
>>>>>>> main
