from django.db import models
# from django.contrib.postgres.fields import ArrayField

from tubes.models import TubeBatch


class Run(models.Model):
    '''
    - barcodes: If tube_batches selected then auto populate
    - tube_batches: may be set to auto populate barcodes field and generate the RUN file
    '''
    title = models.CharField(blank=True, max_length=100)
    # barcodes = ArrayField(blank=True)

    tube_batches = models.ManyToManyField(TubeBatch)

    run_characteristics = models.JSONField()
    well_template = models.JSONField()
    run_file = models.FileField()


class RunResult(models.Model):
    '''
    - prev: multiple results upload may occur
    - data: hold the parsed data
    - barcode_data: hold data grouped by barcode
    ## data: {sampleId:<SAMPLE_ID>, ...scientific values}
    ## barcode_data: {barcode:<BARCODE>, auto_result:<AUTO_RESULT>, updated_result:<USER_RESULT>, ...some main scientific values}
    '''
    run = models.ForeignKey(Run, on_delete=models.PROTECT)
    prev = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

    raw_data = models.JSONField()
    barcode_data = models.JSONField()