from django.test import TestCase

from tubes.models import Tube, TubeBatch, TubeBatchPosition
from .factories import TubeFactory, InternalTubeFactory, TubeBatchFactory

# with open('./unolims/tubes/tests/data/A_scan.csv', newline='') as csvfile:
# ...  reader = csv.DictReader(csvfile)
# ...  for row in reader:
# ...   print(row)

# X : Position filled (default)
# P : Positions of the pooling tube
# - : No tube in position
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
    ['X','X','X','X','X','X','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
]
ROWS = ['A','D','C','D','E','F','G','H','I','J','K','L']


def fill_batch(batch):
    for idx_row, row in enumerate(PLATE_A_POS):
        for idx_col, _ in enumerate(row):
            if 'X' == PLATE_A_POS[idx_row][idx_col]:
                tube = TubeFactory()
            else:
                # P tube is internally provided and tube id differs significantly
                tube = InternalTubeFactory()
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            tbp = TubeBatchPosition.objects.create(tube=tube, batch= batch, position=position)
            # print(tube.tube_id, ' ', position)

def fill_batch_B(batch, tube_ids):
    # set all possible positions in a rack
    positions = []
    for idx_row, row in enumerate(PLATE_B_POS):
        for idx_col, _ in enumerate(row):
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            positions.append(position)
    
    # validate number of tubes - just in case...
    if len(tube_ids) > len(positions): # would be impossible to do - right?
        return

    # put tubes in positions
    for idx, tube_id in enumerate(tube_ids):
        position = positions[idx]
        tube = Tube.objects.get(tube_id=tube_id)
        TubeBatchPosition.objects.create(tube=tube, batch=batch, position=position)
        # print(tube_id, ' ', position)

TAG_POOLING_SCAN = 'PoolingScan'
TAG_RUN_SCAN = 'RunScan'

def add_pooling_tube_batch():
    batch = TubeBatchFactory(xtra_data = {"rack_id":'XXP001'})
    batch.tags.add(TAG_POOLING_SCAN)
    fill_batch(batch)


class TubeBatchOneTestCase(TestCase):
    def test_create_type_A_batch(self):
        add_pooling_tube_batch()
        self.assertEqual(12*8, Tube.objects.count())

    def test_create_type_B_batch(self):
        # create TYPE A batches for the exact amount of positions in one TYPE B batch
        for idx_row, row in enumerate(PLATE_B_POS):
            for idx_col, _ in enumerate(row):
                if '-' != PLATE_B_POS[idx_row][idx_col]:
                    # TYPE A BATCH
                   add_pooling_tube_batch()
        self.assertEqual(12*8*(8*4+6), Tube.objects.count())
        
        # create one type B batch
        run_batch = TubeBatchFactory(xtra_data = {"rack_id":'XXR001'})
        run_batch.tags.add(TAG_RUN_SCAN)
        print('RUN BATCH PK: ', run_batch.pk)

        # find all pooling tubes
        pooling_batches = TubeBatch.objects.filter(tags__name__in=[TAG_POOLING_SCAN])
        print('POOLING BATCHES PK: ', list(pooling_batches.values_list('pk', flat=True)))
        tube_ids = TubeBatchPosition.objects.filter(batch__in=pooling_batches).filter(position='L8').values_list('tube__tube_id', flat=True)
        print('TUBE IDS: ', tube_ids)
        self.assertEqual(8*4+6, len(tube_ids))

        # fill with all P tubes from type A BATCHes
        fill_batch_B(run_batch, tube_ids)

        tube_run_batch = TubeBatch.objects.get(tags__name__in=[TAG_RUN_SCAN])
        self.assertEqual(8*4+6, tube_run_batch.tubes.count())