from django.test import TestCase

from tubes.models import Tube, TubeBatch, TubeBatchPosition
from .factories import TubeFactory, InternalTubeFactory, TubeBatchFactory
from configs import PLATE_A_POS, PLATE_B_POS, ROWS, LEN_ROWS, LEN_COLS, POOLING_TUBE_POS

def fill_batch(batch):
    for idx_row, row in enumerate(PLATE_A_POS):
        for idx_col, _ in enumerate(row):
            if 'X' == PLATE_A_POS[idx_row][idx_col]:
                tube = TubeFactory()
            else:
                # P tube is internally provided and tube id differs significantly
                tube = InternalTubeFactory()
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            TubeBatchPosition.objects.create(tube=tube, batch= batch, position=position)

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
        self.assertEqual(LEN_ROWS*LEN_COLS, Tube.objects.count())

    def test_create_type_B_batch(self):
        # create TYPE A batches for the exact amount of positions in one TYPE B batch
        for idx_row, row in enumerate(PLATE_B_POS):
            for idx_col, _ in enumerate(row):
                if '-' != PLATE_B_POS[idx_row][idx_col]:
                    # TYPE A BATCH
                   add_pooling_tube_batch()
        self.assertEqual(LEN_ROWS*LEN_COLS*(LEN_COLS*4+6), Tube.objects.count())
        
        # create one type B batch
        run_batch = TubeBatchFactory(xtra_data = {"rack_id":'XXR001'})
        run_batch.tags.add(TAG_RUN_SCAN)
        print('RUN BATCH PK: ', run_batch.pk)

        # find all pooling tubes
        pooling_batches = TubeBatch.objects.filter(tags__name__in=[TAG_POOLING_SCAN])
        print('POOLING BATCHES PK: ', list(pooling_batches.values_list('pk', flat=True)))
        tube_ids = TubeBatchPosition.objects.filter(batch__in=pooling_batches).filter(position=POOLING_TUBE_POS).values_list('tube__tube_id', flat=True)
        print('TUBE IDS: ', tube_ids)
        self.assertEqual(LEN_COLS*4+6, len(tube_ids))

        # fill with all P tubes from type A BATCHes
        fill_batch_B(run_batch, tube_ids)

        tube_run_batch = TubeBatch.objects.get(tags__name__in=[TAG_RUN_SCAN])
        self.assertEqual(LEN_COLS*4+6, tube_run_batch.tubes.count())


from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import csv


def fill_batch_with_positions(batch, tube_data_list):
    for tube_data in tube_data_list:
        if 'EMPTY' == tube_data['barcode']:
            continue
        tube = None
        position = tube_data['position']
        if  POOLING_TUBE_POS == position:
            tube = InternalTubeFactory()
        else:
            tube = TubeFactory()
        TubeBatchPosition.objects.create(tube=tube, batch= batch, position=position)


class ReadTubeBatchFileTestCase(TestCase):
    def test_batch_A(self):
        parsed_tubes = []
        rack_id = ''
        with open(BASE_DIR / 'tests/data/A_scan.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                print(row)
                parsed_tubes.append(row)
                rack_id = row['rack_id'] #assume all rack id's are same
        
        self.assertIsNot('', rack_id)

        batch = TubeBatchFactory(xtra_data = {"rack_id":rack_id})
        batch.tags.add(TAG_POOLING_SCAN)
        fill_batch_with_positions(batch, parsed_tubes)
        self.assertEqual(25, Tube.objects.count())


