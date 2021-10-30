from django.core.management.base import BaseCommand, CommandError

from tubes.models import Tube, TubeBatch, TubeBatchPosition
from configs import PLATE_A_POS, PLATE_B_POS, ROWS, LEN_ROWS, LEN_COLS, POOLING_TUBE_POS
from tubes.tests.factories import TubeFactory, InternalTubeFactory, TubeBatchFactory

from .helpers import create_type_a_batch, create_type_b_batch


class Command(BaseCommand):
    help = 'Creates mock Tube batch files - for demo or testing...'

    def handle(self, *args, **options):
        batch_a_list = []
        for pos in range(LEN_ROWS*LEN_COLS):
            batch_a = create_type_a_batch()
            tube_F8 = batch_a.tubes.get(tubebatchposition__position=POOLING_TUBE_POS)
            batch_a_list.append(tube_F8)

        batch = create_type_b_batch(batch_a_list)
        
        self.stdout.write(self.style.SUCCESS('Count "%d"' % Tube.objects.filter(tubebatch=batch).count()))
