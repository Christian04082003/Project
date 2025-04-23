from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('landing/', auth_views.LoginView.as_view(), name='landing'),
    path('Ehub/', views.Ehub, name = 'Ehub'),

    path('loading/', views.loading, name="loading"),
    path('home/', views.home, name="home"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
