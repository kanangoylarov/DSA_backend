# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ScriptsViewSet, SessionsViewSet, BroadcastsViewSet, SyllabusViewSet, TrainerViewSet , ApplyViewSet, ContactViewSet, SubscribeViewSet, TeachersViewSet, GraduatesViewSet

# router = DefaultRouter()
# router.register(r'apply', ApplyViewSet, basename='apply')
# router.register(r'contact', ContactViewSet, basename='contact')
# router.register(r'subscribe', SubscribeViewSet, basename='subscribe')
# router.register(r'scripts', ScriptsViewSet, basename='scripts')
# router.register(r'sessions', SessionsViewSet, basename='sessions')  
# router.register(r'broadcasts', BroadcastsViewSet, basename='broadcasts') 
# router.register(r'syllabus', SyllabusViewSet, basename='syllabus') 
# router.register(r'trainers', TrainerViewSet, basename='trainers')
# router.register(r'teachers', TeachersViewSet, basename='teachers')
# router.register(r'graduates', GraduatesViewSet, basename='graduates')


from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
urlpatterns = [
    # Müraciət URLs
    
    path('müraciət/', MüraciətListView.as_view(), name='müraciət_list'),
    path('müraciət/<int:pk>/', MüraciətDetailView.as_view(), name='müraciət_detail'),
    path('müraciət/create/', MüraciətCreateView.as_view(), name='müraciət_create'),
    path('müraciət/<int:pk>/update/', MüraciətUpdateView.as_view(), name='müraciət_update'),
    path('müraciət/<int:pk>/delete/', MüraciətDeleteView.as_view(), name='müraciət_delete'),

    # Əlaqə URLs
    path('əlaqə/', ƏlaqəListView.as_view(), name='əlaqə_list'),
    path('əlaqə/<int:pk>/', ƏlaqəDetailView.as_view(), name='əlaqə_detail'),
    path('əlaqə/create/', ƏlaqəCreateView.as_view(), name='əlaqə_create'),
    path('əlaqə/<int:pk>/update/', ƏlaqəUpdateView.as_view(), name='əlaqə_update'),
    path('əlaqə/<int:pk>/delete/', ƏlaqəDeleteView.as_view(), name='əlaqə_delete'),

    # Qeydiyyat URLs
    path('qeydiyyat/', QeydiyyatListView.as_view(), name='qeydiyyat_list'),
    path('qeydiyyat/<int:pk>/', QeydiyyatDetailView.as_view(), name='qeydiyyat_detail'),
    path('qeydiyyat/create/', QeydiyyatCreateView.as_view(), name='qeydiyyat_create'),
    path('qeydiyyat/<int:pk>/update/', QeydiyyatUpdateView.as_view(), name='qeydiyyat_update'),
    path('qeydiyyat/<int:pk>/delete/', QeydiyyatDeleteView.as_view(), name='qeydiyyat_delete'),

    # Bootcamps URLs
    path('bootcamps/', BootcampsListView.as_view(), name='bootcamps_list'),
    path('bootcamps/<int:pk>/', BootcampsDetailView.as_view(), name='bootcamps_detail'),
    path('bootcamps/create/', BootcampsCreateView.as_view(), name='bootcamps_create'),
    path('bootcamps/<int:pk>/update/', BootcampsUpdateView.as_view(), name='bootcamps_update'),
    path('bootcamps/<int:pk>/delete/', BootcampsDeleteView.as_view(), name='bootcamps_delete'),

    # BootcampTipi URLs
    path('bootcamptipi/', BootcampTipiListView.as_view(), name='bootcamptipi_list'),
    path('bootcamptipi/<int:pk>/', BootcampTipiDetailView.as_view(), name='bootcamptipi_detail'),
    path('bootcamptipi/create/', BootcampTipiCreateView.as_view(), name='bootcamptipi_create'),
    path('bootcamptipi/<int:pk>/update/', BootcampTipiUpdateView.as_view(), name='bootcamptipi_update'),
    path('bootcamptipi/<int:pk>/delete/', BootcampTipiDeleteView.as_view(), name='bootcamptipi_delete'),

    # Təlimlər URLs
    path('təlimlər/', TəlimlərListView.as_view(), name='təlimlər_list'),
    path('təlimlər/<int:pk>/', TəlimlərDetailView.as_view(), name='təlimlər_detail'),
    path('təlimlər/create/', TəlimlərCreateView.as_view(), name='təlimlər_create'),
    path('təlimlər/<int:pk>/update/', TəlimlərUpdateView.as_view(), name='təlimlər_update'),
    path('təlimlər/<int:pk>/delete/', TəlimlərDeleteView.as_view(), name='təlimlər_delete'),

    # Diğer URL'ler
    # Burada diğer modeller için aynı yapıyı oluşturabilirsiniz.
]

urlpatterns = [
    path('', include(router.urls)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
