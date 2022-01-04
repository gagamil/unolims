import json
from django.db import models

from .services import BatchImportData, parse_batch_data_from_file, get_tube_batch_from_tube_data


class FileImportTubeBatch(models.Model):
    '''
    This is a DTO.
    - tubes are auto generated by parsing the file contents
    - batch_data is the parsed contents 
    # - is_valid set programmatically

    '''
    POOLING_BATCH = 'POOLING_BATCH'
    RUN_BATCH = 'RUN_BATCH'
    BATCH_TYPE_CHOICES = [
        (POOLING_BATCH, 'Pooling batch'),
        (RUN_BATCH, 'Run batch')
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
        self.batch_data = {'tube_data': json.dumps(tube_data)}

