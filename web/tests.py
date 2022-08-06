from pathlib import Path
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APITestCase
from dataclasses import dataclass, asdict, field

from tubes.models import TubeBatch

@dataclass
class RunDTO:
    """Class for creating DTO of a RUN."""
    title: str
    tube_batches: list
    run_characteristics: dict = field(default_factory=dict)

class ImportBatchFile(TestCase):

    def test_file_upload_200(self):
        project_root_dir = Path(settings.BASE_DIR)
        scan = Path('data_importing/test_data/test scan simple.csv')
        file = Path(project_root_dir / scan)

        with open(file) as fp:
            response = self.client.post(reverse('tubebatch-fileimport-create-page'), {'batch_type': 'POOLING_BATCH', 'import_file': fp})
            self.assertEqual(302, response.status_code)


class RunCreateAPITestCase(APITestCase):
    def test_run_create_api_view(self):
        url = reverse('run-create-endpoint')

        from tubes.tests.factories import TubeBatchFactory
        from common.const import TAG_RUN_BATCH
        # create 2 Tube batches
        run_batch_1 = TubeBatchFactory(xtra_data = {"rack_id":'XXR001'})
        run_batch_1.tags.add(TAG_RUN_BATCH)
        run_batch_2 = TubeBatchFactory(xtra_data = {"rack_id":'XXR002'})
        run_batch_2.tags.add(TAG_RUN_BATCH)

        run = RunDTO(title='Test run 1', tube_batches=[run_batch_1.pk, run_batch_2.pk])
        response = self.client.post(url, data=asdict(run), format='json')
        print(response.data)
        self.assertEqual(201, response.status_code)
