from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import History

@receiver(post_save, sender='photo.Photo')
def create_history(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            email=instance.email,
            name=instance.name,
            history_img=instance.image,
            created_at=instance.created_at,
            causation=instance.explain
        )