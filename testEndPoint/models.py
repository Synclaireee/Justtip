from django.db import models
from django.utils import timezone

# Create your models here.

class TestEndpoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='TITLE')
    text1 = models.TextField()
    bool1 = models.BooleanField(default=False)
    int1 = models.IntegerField(default='0')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']