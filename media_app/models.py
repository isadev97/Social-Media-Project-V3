from django.db import models
from authentication.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='profile_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "profile"

# post = Post.objects.get(pk=<ID>)
# post.user => User
# using reverse relationship via related_name
# user = User.objects.get(pk=<ID>)
# user.post => Post

class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(null=True, upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "post"


class LikePost(models.Model):
    user = models.ForeignKey(User, related_name='like_post', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "like_post"
        
        
    