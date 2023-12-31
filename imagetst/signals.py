from . models import Profile
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

@receiver(post_save, sender=User)
def profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance,
            name = instance.username,
            email = instance.email
        )