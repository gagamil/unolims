import logging
from django.dispatch import receiver

from common.signals import tube_batch_import_done
from common.const import TAG_POOLING_BATCH, TAG_RUN_BATCH, POOLING_BATCH
from tubes.models import Tube, TubeBatch, TubeBatchPosition

logger = logging.getLogger(__name__)


@receiver(tube_batch_import_done)
def new_batch_imported(sender, **kwargs):
    tube_batch_data = kwargs['tube_batch_data']
    logger.info(f'SIG Handler will create new Tube batch with id: {tube_batch_data.batch_id}')
    # DO ATOMIC
    xtra_data = {}
    xtra_data['rack_id'] = tube_batch_data.batch_id
    xtra_data['created_at'] = tube_batch_data.timestamp
    batch = TubeBatch.objects.create(xtra_data=xtra_data, title=tube_batch_data.title)

    if POOLING_BATCH == tube_batch_data.batch_type:
        batch.tags.add(TAG_POOLING_BATCH)
    else:
        batch.tags.add(TAG_RUN_BATCH)

    for t in tube_batch_data.tubes:
        tube = Tube.objects.create(tube_id=t.barcode)
        TubeBatchPosition.objects.create(tube=tube, batch=batch, position=t.position)
