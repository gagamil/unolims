from rest_framework import generics
from rest_framework import serializers

from tubes.models import TubeBatch

class TubeBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeBatch
        fields = ['title']


class UpdateTubeBatchAPIView(generics.UpdateAPIView):
    queryset = TubeBatch.objects.all()
    serializer_class = TubeBatchSerializer