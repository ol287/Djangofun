from django.db import models
from django.contrib.auth.models import User

# Model for a blog post
class Post(models.Model):
    # Title of the post
    title = models.CharField(max_length=100)
    # Content of the post
    content = models.TextField()
    # Date when the post was created (automatically set)
    date_posted = models.DateTimeField(auto_now_add=True)
    # Author of the post (linked to a user)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # String representation of the model
    def __str__(self):
        return self.title
