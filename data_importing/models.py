import json
from django.db import models

from .services import parse_batch_data_from_file, get_tube_batch_from_tube_data
from common.const import TAG_POOLING_BATCH, TAG_RUN_BATCH, POOLING_BATCH, RUN_BATCH
from tubes.models import TubeBatch

class FileImportTubeBatch(models.Model):
    '''
    This is a DTO.
    - tubes are auto generated by parsing the file contents
    - batch_data is the parsed contents 
    # - is_valid set programmatically

    '''
    BATCH_TYPE_CHOICES = [
        (POOLING_BATCH, TAG_POOLING_BATCH),
        (RUN_BATCH, TAG_RUN_BATCH)
    ]
    batch_type = models.CharField(choices=BATCH_TYPE_CHOICES,
        default=POOLING_BATCH, max_length=32)
    import_file = models.FileField(upload_to='import_batch')

    batch_data = models.JSONField()

    # is_valid = models.BooleanField()
    
    def clean(self) -> None:
        '''
        Copy the data into JSON field
        '''
        super().clean()
        tube_data = []
        tube_data = parse_batch_data_from_file(full_file = self.import_file.file)
        tube_batch = get_tube_batch_from_tube_data(tube_data=tube_data, batch_type=self.batch_type)
        self.batch_data = {'tube_data': tube_batch.to_json()}


class APIImportRun(models.Model):
    '''
    This is a DTO
    '''
    title = models.CharField(blank=True, max_length=100)
    tube_batches = models.ManyToManyField(TubeBatch)
    run_characteristics = models.JSONField()