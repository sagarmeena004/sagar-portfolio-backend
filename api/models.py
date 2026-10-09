from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Python Development', 'Python Development'),
        ('Data Analytics', 'Data Analytics'),
        ('Web Development', 'Web Development'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Web Development'
    )

    featured = models.BooleanField(default=False)

    highlights = models.JSONField(default=list, blank=True)

    tech = models.JSONField(default=list, blank=True)

    image = models.URLField(blank=True)

    project_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"