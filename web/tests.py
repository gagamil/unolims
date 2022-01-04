from pathlib import Path
from django.test import TestCase
from django.conf import settings
from django.urls import reverse


class ImportBatchFile(TestCase):

    def test_file_upload_200(self):
        project_root_dir = Path(settings.BASE_DIR)
        scan = Path('data_importing/test_data/test scan simple.csv')
        file = Path(project_root_dir / scan)

        with open(file) as fp:
            response = self.client.post(reverse('tubebatch-fileimport-create-page'), {'batch_type': 'POOLING_BATCH', 'import_file': fp})
            self.assertEqual(302, response.status_code)