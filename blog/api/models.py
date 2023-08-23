from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Post/Blog Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'post'

# Like Model
class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' liked by - ' + self.user.name