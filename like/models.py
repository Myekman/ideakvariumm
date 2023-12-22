from django.db import models
from django.contrib.auth.models import User
from fishes.models import Fish

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fish_post = models.ForeignKey(
        Fish, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # unique_together specifies that the combination of user and post should be unique, 
    # meaning a user can only like a particular post once.
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'fish_post']

    def __str__(self):
        return f'{self.user} {self.fish_post}'