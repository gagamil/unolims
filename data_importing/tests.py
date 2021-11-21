
from pathlib import Path
from django.test import TestCase
from django.conf import settings

from .services import parse_batch_data_from_file, get_tube_batch_from_tube_data


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
        tube_batch = get_tube_batch_from_tube_data(tube_data=tube_data)
        self.assertEqual(5, len(tube_batch.tubes))
        self.assertEqual('RR00012345', tube_batch.batch_id)

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
        tube_batch = get_tube_batch_from_tube_data(tube_data=tube_data)
        self.assertIsNone(tube_batch)
