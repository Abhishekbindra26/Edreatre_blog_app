from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def get_summary(self):
        """Return a short preview of the post content"""
        words = self.content.split()
        if len(words) > 30:
            return ' '.join(words[:30]) + '...'
        return self.content