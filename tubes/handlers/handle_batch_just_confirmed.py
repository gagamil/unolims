from django.dispatch import receiver
from tubes.signals import batch_just_confirmed


@receiver(batch_just_confirmed)
def batch_just_confirmed(sender, **kwargs):
    batch_id = kwargs['batch_id']
    print(f'Batch {batch_id} just been confirmed')
