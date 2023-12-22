from django.db import models

# signals handle the like count
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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
        return f'{self.user} {self.fish_post} {self.like_count}'

# handle the likes count
@receiver(post_save, sender=Like)
@receiver(post_delete, sender=Like)
def update_like_count(sender, instance, **kwargs):
    fish_instance = instance.fish_post
    fish_instance.like_count = Like.objects.filter(fish_post=fish_instance).count()
    fish_instance.save()