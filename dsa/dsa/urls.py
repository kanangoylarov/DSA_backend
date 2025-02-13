from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import ApplyViewSet, ContactViewSet, SubscribeViewSet, success_view, apply_view, contacts_view


router = DefaultRouter()
router.register(r'apply', ApplyViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'subscribe', SubscribeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoint'leri burada
    path("api/apply/", apply_view, name="apply"),
    path("api/contacts/", contacts_view, name="contact"),  # Burada hata düzeltilmiş
    path('api/success/', success_view, name='success'),
]