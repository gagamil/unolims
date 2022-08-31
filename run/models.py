from django.db import models

from common.data import Tube, RunData


class Run(models.Model):
    '''
    - barcodes: List of common.data.Tube dataclass objects
    # - run_xtra_data: denormalized data related to the TubeBatch
    '''
    title = models.CharField(blank=True, max_length=100)
    barcodes = models.JSONField()
    run_characteristics = models.JSONField()
    run_xtra_data = models.JSONField()

class RunConfiguration(models.Model):
    run = models.OneToOneField(Run, on_delete=models.PROTECT)
    well_template = models.JSONField()
    run_file = models.FileField()

# class RunResultFile(models.Model):
#     run = models.ForeignKey(Run)
#     results_file = models.FileField()

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