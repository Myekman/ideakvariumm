from django.db import models
from django.contrib.auth.models import User
from fishes.models import Fish

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fish_post = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name='likes_count')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
    unique_together = ('user', 'fish_post')