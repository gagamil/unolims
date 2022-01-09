import django.dispatch

from common.data import TubesBatchData

tube_batch_import_done = django.dispatch.Signal()
def sig_send__tube_batch_data_import_done(*, sender, sender_pk: int, tube_batch_data: TubesBatchData) -> None:
    print(sender, sender_pk, tube_batch_data)
    tube_batch_import_done.send(sender=sender, sender_pk=sender_pk, tube_batch_data=tube_batch_data)