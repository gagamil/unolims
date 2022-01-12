from django.urls import path, include

from .views import TubeBatchListView, TubeBatchDetailView, TubeBatchFileImportCreateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('', TubeBatchListView.as_view(), name='tubebatch-list-page'),
    path('<int:pk>', TubeBatchDetailView.as_view(), name='tubebatch-detail-page'),

    path('import/tubebatch/', TubeBatchFileImportCreateView.as_view(), name='tubebatch-fileimport-create-page'),
]