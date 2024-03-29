from pipes import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.db.models import Q
from django.urls import reverse
import django_filters
from django_filters.views import FilterView
from taggit.models import Tag

from common.signals import sig_send__tube_batch_data_import_done
from common.data import TubesBatchData
from tubes.models import Tube, TubeBatch, TubeBatchPosition
from data_importing.models import FileImportTubeBatch
from run.models import Run


# class TubeBatchFilter(django_filters.FilterSet):
#     class Meta:
#         model = TubeBatch
#         fields = ['title', 'tubes__barcode']

class TubeBatchFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='tubebatch_filter',label="Search")

    class Meta:
        model = TubeBatch
        fields = ['q']

    def tubebatch_filter(self, queryset, name, value):
        return TubeBatch.objects.filter(
            Q(title__icontains=value) | Q(xtra_data__icontains=value) |Q(tubes__barcode__icontains=value)
        )


class TubeBatchListView(LoginRequiredMixin, FilterView):
    model = TubeBatch
    filterset_class = TubeBatchFilter
    template_name_suffix = '_list'
    paginate_by = 25

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


class TubeBatchDetailView(LoginRequiredMixin, DetailView):
    model = TubeBatch

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['js_data'] = {'title':self.object.title, 'id':self.object.pk}
        return context


class TubeBatchFileImportCreateView(LoginRequiredMixin, CreateView):
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
        return redirect_url


class CreateRunTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'run/create_run.html'
