from django.dispatch import receiver
from tubes.signals import batch_pending_confirmation


@receiver(batch_pending_confirmation)
def batch_pending_confirmation(sender, **kwargs):
    batch_id = kwargs['batch_id']
    print(f'Batch {batch_id} pending confirmation')
