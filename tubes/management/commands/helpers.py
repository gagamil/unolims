import string
import random
import datetime

from tubes.models import Tube, TubeBatch, TubeBatchPosition
from configs import PLATE_A_POS, PLATE_B_POS, ROWS, LEN_ROWS, LEN_COLS, POOLING_TUBE_POS
from tubes.tests.factories import TubeFactory, InternalTubeFactory, TubeBatchFactory


def random_digits():
    return ''.join(random.choices(string.digits + string.digits, k=6))


def create_type_b_batch(tubes):
    print('Tubes: ', tubes)
    title_date = datetime.date.today().strftime('%A %d')
    timestamp = datetime.datetime.now()
    batch = TubeBatchFactory(xtra_data={'rack_id':f'RACK_{random_digits()}','created_at': timestamp.isoformat()}, title=f'{title_date} batch')
    batch.tags.add('RunScan')

    count = 1
    for idx_row, row in enumerate(PLATE_B_POS):
        for idx_col, _ in enumerate(row):
            if PLATE_B_POS[idx_row][idx_col] == '-':
                continue
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            TubeBatchPosition.objects.create(tube=tubes[count], batch= batch, position=position)

            count += 1
    return batch


def create_type_a_batch():
    title_date = datetime.date.today().strftime('%A %d')
    timestamp = datetime.datetime.now()
    batch_a = TubeBatchFactory(xtra_data={'rack_id':f'RACK_{random_digits()}', 'created_at': timestamp.isoformat()}, title=f'{title_date} batch')
    batch_a.tags.add('PoolingScan')

    # create N (batch_a_tubes_count) tubes
    batch_a_tubes_count = random.randint(3, LEN_ROWS*LEN_COLS-1)
    for idx_row, row in enumerate(PLATE_A_POS):
        get_out = False
        for idx_col, _ in enumerate(row):
            if batch_a_tubes_count == idx_row + idx_col:
                get_out = True
                break

            if 'X' == PLATE_A_POS[idx_row][idx_col]:
                tube = TubeFactory()
            else:
                # P tube is internally provided and tube id differs significantly
                tube = InternalTubeFactory()
            position = '%s%d' % (ROWS[idx_row], idx_col+1)
            TubeBatchPosition.objects.create(tube=tube, batch= batch_a, position=position)
        if get_out:
            break
    
    if not TubeBatchPosition.objects.filter(batch=batch_a, position=POOLING_TUBE_POS).exists():
        # assume that at POOLING_TUBE_POS there should be an Internal barcoded tube
        tube = InternalTubeFactory()
        TubeBatchPosition.objects.create(tube=tube, batch= batch_a, position=POOLING_TUBE_POS)
    
    return batch_a