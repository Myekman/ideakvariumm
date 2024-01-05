from django.db import models
from django.contrib.auth.models import User

class Fish(models.Model):
    FISH_TYPES = [
        ('goldfish', 'Goldfish'),
        ('clownfish', 'Clownfish'),
        ('anglerfish', 'Anglerfish'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    # like_count = models.IntegerField(default=0)
    fish_type = models.CharField(max_length=20, choices=FISH_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_fish_type_display()} #{self.id}: {self.message} {self.user}"