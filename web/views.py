from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.urls import reverse
import django_filters
from django_filters.views import FilterView
from taggit.models import Tag
from actstream import action

from common.signals import sig_send__tube_batch_data_import_done
from common.data import TubesBatchData
from tubes.models import Tube, TubeBatch, TubeBatchPosition
from data_importing.models import FileImportTubeBatch


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


class TubeBatchFileImportCreateView(CreateView):
    model = FileImportTubeBatch
    fields = ['batch_type', 'import_file']
    template_name = 'tubes/tubebatch_fileimport.html'
    
    def get_success_url(self):
        return reverse('tubebatch-list-page')

    def form_valid(self, form):
        redirect_url = super().form_valid(form)
        batch_data = self.object.batch_data
        import_id = self.object.pk

        batch_data= TubesBatchData.from_json(batch_data['tube_data'])
        sig_send__tube_batch_data_import_done(sender=TubeBatchFileImportCreateView.__class__.__name__, sender_pk=import_id, tube_batch_data=batch_data)
        action.send(self.object, verb=f'finished import of new batch of tubes with rack id: {batch_data.batch_id}')
        return redirect_url