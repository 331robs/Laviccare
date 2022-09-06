from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS =(
    (0,"Draft"),
    (1,"publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #for codemy
   # header_image = models.ImageField(null=True,blank=True,upload_to='images/')




    #these are my changes made
    image_title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title