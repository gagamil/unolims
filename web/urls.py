from django.urls import path, include

from .views import TubeBatchListView, TubeBatchDetailView, TubeBatchFileImportCreateView
from .views_rest import UpdateTubeBatchAPIView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('v1/tubebatch/<int:pk>/', UpdateTubeBatchAPIView.as_view(), name='tubebatch-update-endpoint'),
    path('', TubeBatchListView.as_view(), name='tubebatch-list-page'),
    path('<int:pk>', TubeBatchDetailView.as_view(), name='tubebatch-detail-page'),

    path('import/tubebatch/', TubeBatchFileImportCreateView.as_view(), name='tubebatch-fileimport-create-page'),
]