from django.dispatch import receiver

from common.signals import tube_batch_import_done
from common.data import TubePositionData, TubesBatchData
from tubes.models import Tube, TubeBatch, TubeBatchPosition


@receiver(tube_batch_import_done)
def new_batch_imported(sender, **kwargs):
    tube_batch_data = kwargs['tube_batch_data']

    # DO ATOMIC
    xtra_data = {}
    xtra_data['rack_id'] = tube_batch_data.batch_id
    batch = TubeBatch.objects.create(tags=tube_batch_data.batch_type, xtra_data=xtra_data)
    for t in tube_batch_data.tubes:
        tube = Tube.objects.create(tube_id=t.barcode)
        TubeBatchPosition.objects.create(tube=tube, batch=batch, position=t.position)
