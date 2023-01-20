from tubes.models import Tube, TubeBatchPosition
from .factories import TubeFactory, InternalTubeFactory, TubeBatchFactory
from configs import PLATE_A_POS, PLATE_B_POS, ROWS
from common.const import TAG_POOLING_BATCH


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

def fill_batch_B(batch, barcodes):
    # set all possible positions in a rack
    positions = []
    for idx_row, row in enumerate(PLATE_B_POS):
        for idx_col, _ in enumerate(row):
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            positions.append(position)
    
    # validate number of tubes - just in case...
    if len(barcodes) > len(positions): # would be impossible to do - right?
        return

    # put tubes in positions
    for idx, barcode in enumerate(barcodes):
        position = positions[idx]
        tube = Tube.objects.get(barcode=barcode)
        TubeBatchPosition.objects.create(tube=tube, batch=batch, position=position)
        # print(barcode, ' ', position)

# TAG_POOLING_SCAN = 'PoolingScan'
TAG_RUN_SCAN = 'RunScan'

def add_pooling_tube_batch():
    batch = TubeBatchFactory(xtra_data = {"rack_id":'XXP001'})
    batch.tags.add(TAG_POOLING_BATCH)
    fill_batch(batch)