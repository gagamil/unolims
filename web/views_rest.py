from rest_framework import generics, views, response
from rest_framework import serializers

from tubes.models import TubeBatch, TubeBatchPosition
from common.signals import sig_send__run_data_import_done
from common.data import Tube, RunData


### TUBES
class TubeBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeBatch
        fields = ['title']


class UpdateTubeBatchAPIView(generics.UpdateAPIView):
    queryset = TubeBatch.objects.all()
    serializer_class = TubeBatchSerializer


class TubeBatchPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeBatchPosition
        fields = ['tube', 'batch', 'position']

class TubeBatchListReadSerializer(serializers.ModelSerializer):
    tubebatchposition_set = TubeBatchPositionSerializer(many=True)
    class Meta:
        model = TubeBatch
        fields = ['id', 'title', 'tubebatchposition_set', 'xtra_data']

def convertAPIBatchTypeToTubeBAtchType(batchType):
    return 'Run Batch'
class TubeBatchListAPIView(generics.ListAPIView):
    def get_queryset(self):
        batchType = self.request.query_params.get('batchType', '')
        tube_batch_list = TubeBatch.objects.all()
        if batchType:
            batch_tag = convertAPIBatchTypeToTubeBAtchType(batchType)
            tube_batch_list = tube_batch_list.filter(tags__name__in=[batch_tag])
        return tube_batch_list

    serializer_class = TubeBatchListReadSerializer

### RUNS

from data_importing.models import APIImportRun
class RunCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIImportRun
        fields = ('title', 'tube_batches', 'run_characteristics')

class CreateRunAPIView(generics.CreateAPIView):
    serializer_class = RunCreateSerializer

    def perform_create(self, serializer):
        imported_run = serializer.save()

        all_tubes = []
        for tube_batch in imported_run.tube_batches.all():
            all_tubes.extend(tube_batch.tubes.all())

        tube_data_list = []
        for tube in all_tubes:
            t = Tube.from_json(tube)
            tube_data_list.append(t)
    
        run_data = RunData(id=imported_run.pk, title=imported_run.title, tubes=tube_data_list, run_characteristics=imported_run.run_characteristics)
        import_id = imported_run.pk
        sig_send__run_data_import_done(sender=CreateRunAPIView.__class__.__name__, sender_pk=import_id, run_data=run_data)


