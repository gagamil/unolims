import logging
from django.dispatch import receiver

from common.signals import run_import_done
# from common.const import TAG_POOLING_BATCH, TAG_RUN_BATCH, POOLING_BATCH
from run.models import Run

logger = logging.getLogger(__name__)


@receiver(run_import_done)
def new_run_imported(sender, **kwargs):
    run_data = kwargs['run_data']
    logger.info(f'SIG Handler will create new Run with id: {run_data.id}')
    # DO ATOMIC

    run = Run.objects.create(title=run_data.title, barcodes=run_data.tubes, run_characteristics=run_data.run_characteristics, run_xtra_data={'source_id':run_data.id})
    run.run_xtra_data = {'origin__uuid':run_data.id}
    run.save()
