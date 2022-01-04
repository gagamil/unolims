from django.forms import ModelForm

from data_importing.models import FileImportTubeBatch


class TubeBatchForm(ModelForm):
    class Meta:
        model = FileImportTubeBatch
        fields = ['import_file', 'batch_type']