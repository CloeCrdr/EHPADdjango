from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'LiveApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('a-propos/', views.about, name='about'),
    path('success/', views.success, name='success'),
    
    path('admin_ehpad/', views.admin, name='admin_ehpad'),
    path('admin_ehpad/create/', views.create_service, name="create_service"),
    path('admin_ehpad/update/<int:id>', views.update_service, name='update_service'),
    path('admin_ehpad/delete/<int:id>', views.delete_service, name='delete_service'),
]