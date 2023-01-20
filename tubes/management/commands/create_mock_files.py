import string
import random
from dataclasses import dataclass

from django.core.management.base import BaseCommand, CommandError
from tubes.models import Tube, TubeBatch, TubeBatchPosition
from configs import PLATE_A_POS, PLATE_B_POS, ROWS, LEN_ROWS, LEN_COLS, POOLING_TUBE_POS
from tubes.tests.factories import TubeFactory, InternalTubeFactory, TubeBatchFactory
from data_importing.const import FILE_HEADERS

def random_digits():
    return ''.join(random.choices(string.digits + string.digits, k=6))


@dataclass
class Tube:
    barcode: str
    position: str


class Command(BaseCommand):
    help = 'Creates mock Tube batch files - for demo or testing...'

    def handle(self, *args, **options):
        # 
        # TYPE A Batch
        batch_a = TubeBatchFactory(xtra_data={'rack_id':f'RACK{random_digits}'})
        batch_a.tags.add('PoolingScan')
        tubes = []
        # create N (batch_a_tubes_count) tubes
        batch_a_tubes_count = random.randint(3, LEN_ROWS*LEN_COLS-1)
        for idx_row, row in enumerate(PLATE_A_POS):
            get_out = False
            for idx_col, _ in enumerate(row):
                if batch_a_tubes_count == idx_row + idx_col:
                    get_out = True
                    break

                position = '%s%d' % (ROWS[idx_row], idx_col+1)
                barcode = f'INXX{random.randint(100000, 999999)}' if 'P' == PLATE_A_POS[idx_row][idx_col] else f'EXTXX{random.randint(100000, 999999)}'
                tubes.append(Tube(barcode=barcode, position=position))
            if get_out:
                break
        
        for t in tubes:
            if t.position == POOLING_TUBE_POS:
                break
        else:
            tubes.append(Tube(barcode=barcode, position=POOLING_TUBE_POS))

        rack_id = f'RACK{random_digits()}'
        from datetime import datetime
        now = datetime.now()
        time = now.strftime("%I:%M:%S %p")
        date =  now.strftime("%m/%d/%Y")
        time_file = now.strftime("%I:%M:%S_%p")
        date_file =  now.strftime("%m_%d_%Y")
        import csv
        from django.conf import settings
        with open(settings.MEDIA_ROOT / 'mock' / f'{date_file}_{time_file}.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FILE_HEADERS, delimiter=';')

            writer.writeheader()
            for tube in tubes:
                writer.writerow({'Date':date, 'Time':time, 'Rack barcode':rack_id, 'Position': tube.position, 'Tube barcode': tube.barcode})

        self.stdout.write(self.style.SUCCESS('Count "%d"' % len(tubes)))
