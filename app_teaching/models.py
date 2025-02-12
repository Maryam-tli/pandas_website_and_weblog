from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)  # نام تگ (مثل Data Analysis, Indexing)

    def __str__(self):
        return self.name


class PandasClass(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    content = models.TextField()
    example_code = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True) 
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
