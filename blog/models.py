from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    post_text = models.TextField(default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    detail_image = models.ImageField(blank=True, null=True)
    extra_img_one = models.ImageField(blank=True, null=True)
    extra_img_two = models.ImageField(blank=True, null=True)
    visited = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
		
    def __str__(self):
        return self.title	

class Page(models.Model):
    main_text = models.TextField()
    visited = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)
    top_image_left = models.ImageField(blank=True, null=True)
    top_image_right = models.ImageField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.main_text 