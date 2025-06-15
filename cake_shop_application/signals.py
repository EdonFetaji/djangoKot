import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Baker,Cake


@receiver(pre_delete, sender=Baker)
def distribute_deleted_baker_cakes(sender, instance, **kwargs):
    baker_cakes = Cake.objects.filter(baker=instance).all()

    if not baker_cakes: return

    other_bakers = Baker.objects.exclude(pk=instance.pk)

    for cake in baker_cakes:
        cake.baker = random.choice(other_bakers)
        cake.save()
