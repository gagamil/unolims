from django.urls import path, include

from .views import TubeBatchListView, TubeBatchDetailView, TubeBatchFileImportCreateView
from .views_rest import UpdateTubeBatchAPIView, TubeBatchListAPIView, CreateRunAPIView
from .views import CreateRunTemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    # REST API
    path('v1/tubebatch/<int:pk>/', UpdateTubeBatchAPIView.as_view(), name='tubebatch-update-endpoint'),
    path('v1/tubebatch/', TubeBatchListAPIView.as_view(), name='tubebatch-list-endpoint'),
    path('v1/run/create/', CreateRunAPIView .as_view(), name='run-create-endpoint'),

    # Django Template views
    path('', TubeBatchListView.as_view(), name='tubebatch-list-page'),
    path('<int:pk>', TubeBatchDetailView.as_view(), name='tubebatch-detail-page'),

    path('import/tubebatch/', TubeBatchFileImportCreateView.as_view(), name='tubebatch-fileimport-create-page'),

    path('run/create/', CreateRunTemplateView.as_view(), name='run-create-page')
]
