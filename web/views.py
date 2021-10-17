from django.views.generic import ListView, DetailView
from django.db.models import Q
import django_filters
from django_filters.views import FilterView

from tubes.models import Tube, TubeBatch, TubeBatchPosition


# class TubeBatchFilter(django_filters.FilterSet):
#     class Meta:
#         model = TubeBatch
#         fields = ['title', 'tubes__tube_id']

class TubeBatchFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='tubebatch_filter',label="Search")

    class Meta:
        model = TubeBatch
        fields = ['q']

    def tubebatch_filter(self, queryset, name, value):
        return TubeBatch.objects.filter(
            Q(title__icontains=value) | Q(xtra_data__icontains=value)
        )


class TubeBatchListView(FilterView):
    model = TubeBatch
    filterset_class = TubeBatchFilter
    template_name_suffix = '_list'

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     batch_filtered_list = TubeBatchFilter(self.request.GET, queryset=qs)
    #     return batch_filtered_list.qs


class TubeBatchDetailView(DetailView):
    model = TubeBatch