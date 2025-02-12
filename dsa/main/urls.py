from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_view, name='apply_form'),
    path('contact/', views.contact_view, name='contact_form'),
    path('subscribe/', views.subscribe_view, name='subscribe_form'),
    path('success/', views.success_view, name='success'),
]
