from django.urls import path
from .views import ProjectListCreateView, ContactCreateView, health_check

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='projects'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('health/', health_check, name='health'),
]