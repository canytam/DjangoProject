from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    createDate = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    message = models.TextField()
    
    class Meta:
        ordering = ['-createDate']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    createTime = models.DateTimeField()
    message = models.TextField()
    
    class Meta:
        ordering = ['createTime']
        
    def __str__(self):
        return self.message[0:75]
    
    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])