from django.urls import path
from .views import ProjectListCreateView, ContactCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='projects'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]