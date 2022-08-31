import logging
import django.dispatch

from common.data import TubesBatchData, RunData

logger = logging.getLogger(__name__)

tube_batch_import_done = django.dispatch.Signal()
def sig_send__tube_batch_data_import_done(*, sender, sender_pk: int, tube_batch_data: TubesBatchData) -> None:
    logger.info(f'SIG "tube_batch_import_done" will be sent with imported tube data. Import ID: sender_pk {tube_batch_data.batch_id}')
    tube_batch_import_done.send(sender=sender, sender_pk=sender_pk, tube_batch_data=tube_batch_data)

run_import_done = django.dispatch.Signal()
def sig_send__run_data_import_done(*, sender, sender_pk: int, run_data: RunData) -> None:
    logger.info(f'SIG "run_import_done" will be sent with imported run data. Import ID: {sender_pk=}')
    run_import_done.send(sender=sender, sender_pk=sender_pk, run_data=run_data)
