from django.contrib import admin
from .models import Project, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at')

    search_fields = ('title', 'description', 'category')

    list_filter = ('category', 'featured', 'created_at')

    ordering = ('-created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'created_at')

    search_fields = ('name', 'email', 'message')

    list_filter = ('created_at',)

    ordering = ('-created_at',)

    readonly_fields = ('created_at',)