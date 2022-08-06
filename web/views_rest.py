from rest_framework import generics, views, response
from rest_framework import serializers

from tubes.models import TubeBatch, TubeBatchPosition

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

from run.models import Run
class RunCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('title', 'tube_batches', 'run_characteristics')

class CreateRunAPIView(generics.CreateAPIView):
    serializer_class = RunCreateSerializer


