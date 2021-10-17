import string
import random

from django.core.management.base import BaseCommand, CommandError
from tubes.models import Tube, TubeBatch, TubeBatchPosition
from configs import PLATE_A_POS, PLATE_B_POS, ROWS, LEN_ROWS, LEN_COLS, POOLING_TUBE_POS
from tubes.tests.factories import TubeFactory, InternalTubeFactory, TubeBatchFactory


def random_digits():
    return ''.join(random.choices(string.digits + string.digits, k=6))


class Command(BaseCommand):
    help = 'Creates mock Tube batch files - for demo or testing...'

    def handle(self, *args, **options):
        # 
        # TYPE A Batch
        batch_a = TubeBatchFactory(xtra_data={'rack_id':f'RACK_{random_digits()}'})
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
            self.stdout.write(self.style.SUCCESS('No pooling tube'))
            tube = InternalTubeFactory()
            TubeBatchPosition.objects.create(tube=tube, batch= batch_a, position=POOLING_TUBE_POS)
        
        self.stdout.write(self.style.SUCCESS('Count "%d"' % Tube.objects.filter(tubebatch=batch_a).count()))
