from rest_framework import generics
from django.http import JsonResponse
from .models import Project, Contact
from .serializers import ProjectSerializer, ContactSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Django backend is running"
    })