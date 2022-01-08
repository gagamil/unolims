
from pathlib import Path
from django.test import TestCase
from django.conf import settings

from .services import parse_batch_data_from_file, get_tube_batch_from_tube_data
from common.const import POOLING_BATCH


class FileImportTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_parsing_OK(self):
        project_root_dir = Path(settings.BASE_DIR)
        scan = Path('data_importing/test_data/test scan simple.csv')
        file = Path(project_root_dir / scan)

        tube_data = []
        # test raw data from import
        with open(file, newline='') as csvfile:
            tube_data = parse_batch_data_from_file(full_file=csvfile)
        self.assertEqual(5, len(tube_data))

        # test tube data in dataclass
        tube_batch = get_tube_batch_from_tube_data(tube_data=tube_data, batch_type=POOLING_BATCH)
        self.assertEqual(5, len(tube_batch.tubes))
        self.assertEqual('RR00012345', tube_batch.batch_id)
        # self.assertEqual(tube_batch.to_json(), '{"batch_id": "RR00012345", "timestamp": "2021-10-13T00:55:33", "tubes": [{"barcode": "TT00011111", "position": "A1"}, {"barcode": "TT00011112", "position": "A2"}, {"barcode": "TT00011113", "position": "A3"}, {"barcode": "TT00011114", "position": "A4"}, {"barcode": "TT00011115", "position": "A5"}]}')

    def test_parsing_ERROR(self):
        project_root_dir = Path(settings.BASE_DIR)
        scan = Path('data_importing/test_data/non_valid_test_scan.csv')
        file = Path(project_root_dir / scan)

        tube_data = []
        # test raw data from import
        with open(file, newline='') as csvfile:
            tube_data = parse_batch_data_from_file(full_file=csvfile)
        self.assertEqual(5, len(tube_data))

        # test tube data in dataclass
        tube_batch = get_tube_batch_from_tube_data(tube_data=tube_data, batch_type=POOLING_BATCH)
        self.assertIsNone(tube_batch)
