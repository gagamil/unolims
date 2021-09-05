from django.test import TestCase

from .models import Tube, TubeBatch, TubeBatchPosition
from .factories import TubeFactory, TubeBatchFactory

COLS = range(12)
ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
BATCH_1_CONFIG = {"name":'Pooling Scan', "tube_count":32, "positions":"A1:H12"}
BATCH_2_CONFIG = {"name":'Sample Scan', "tube_count":32, "positions":"A1:H12"}

PLATE_A_POS = [
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','P',],
]
PLATE_B_POS = [
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
    ['X','X','X','X','X','X','X','X',],
]
ROWS = ['A','D','C','D','E','F','G','H','I','J','K','L']
# Create your tests here.


def fill_batch(batch):
    for idx_row, row in enumerate(PLATE_A_POS):
        for idx_col, col in enumerate(row):
            tube = TubeFactory()
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            tbp = TubeBatchPosition.objects.create(tube=tube, batch= batch, position=position)
            print(tube.tube_id, ' ', position)


class TubeBatchOneTestCase(TestCase):
    def test_create_type_A_batch(self):
        batch = TubeBatchFactory(xtra_data = {"rack_id":'XXP001'})
        batch.tags.add('PoolingScan')
        fill_batch(batch)

    def test_create_type_B_batch(self):
        batch_1 = TubeBatchFactory(xtra_data = {"rack_id":'XXY001'})
        batch_1.tags.add('RunScan')
        fill_batch(batch_1)
