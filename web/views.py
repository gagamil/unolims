from django.views.generic import ListView, DetailView
from django.db.models import Q
import django_filters
from django_filters.views import FilterView
from taggit.models import Tag

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
            Q(title__icontains=value) | Q(xtra_data__icontains=value) |Q(tubes__tube_id__icontains=value)
        )


class TubeBatchListView(FilterView):
    model = TubeBatch
    filterset_class = TubeBatchFilter
    template_name_suffix = '_list'

    def get_queryset(self):
        qs = self.model.objects.all()
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__name__in=[tag])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tabs'] = Tag.objects.all()
        return context


class TubeBatchDetailView(DetailView):
    model = TubeBatch