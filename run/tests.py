from django.test import TestCase

from tubes.tests.factories import TubeFactory
from .models import Run
from .const import RUN_REPLICATION__DUPLICATE, RUN_REPLICATION__DUPLICATE__PATTERN, \
    RUN_REPLICATION__TRIPLICATE, RUN_REPLICATION__TRIPLICATE__PATTERN, \
    RUN_WELLPLATE__384, RUN_WELLPLATE__384_LAYOUT, RUN_WELLPLATE__CONFIGS, ALPHABET, RUN_METHOD_TARGETS__SALIVECLEAR
from .services import create_well_plate_template,  get_wells_with_pattern_mask


# def create_run_with_barcodes(*, barcodes, run_method):
#     Run.objects.create(barcodes=barcodes,run_characteristics, well_template, run_file)
class RunCreateTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_build_wells(self):
        barcodes = [TubeFactory() for x in range(36)]
        config = next(item for item in RUN_WELLPLATE__CONFIGS if item["name"] == RUN_WELLPLATE__384)
        layout = config['layout']
        well_count = layout['well_count']
        rows = layout['rows']
        row_max_idx = ALPHABET.index(rows[1])

        # run_pk = create_run_with_barcodes(barcodes=barcodes, run_method=RUN_METHOD__SALIVECLEAR)
        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__DUPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__DUPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx)
        expected_wells = [['A0', 'A1'], ['B0', 'B1'], ['C0', 'C1'], ['D0', 'D1'], ['E0', 'E1'], ['F0', 'F1'], ['G0', 'G1'], ['H0', 'H1'], ['I0', 'I1'], ['J0', 'J1'], ['K0', 'K1'], ['L0', 'L1'], ['M0', 'M1'], ['N0', 'N1'], ['O0', 'O1'], ['A2', 'A3'], ['B2', 'B3'], ['C2', 'C3'], ['D2', 'D3'], ['E2', 'E3'], ['F2', 'F3'], ['G2', 'G3'], ['H2', 'H3'], ['I2', 'I3'], ['J2', 'J3'], ['K2', 'K3'], ['L2', 'L3'], ['M2', 'M3'], ['N2', 'N3'], ['O2', 'O3'], ['A4', 'A5'], ['B4', 'B5'], ['C4', 'C5'], ['D4', 'D5'], ['E4', 'E5'], ['F4', 'F5']]
        self.assertEqual(expected_wells, wells)

        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__TRIPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx)
        expected_wells = [['A0', 'A1', 'B1'], ['C0', 'C1', 'D1'], ['E0', 'E1', 'F1'], ['G0', 'G1', 'H1'], ['I0', 'I1', 'J1'], ['K0', 'K1', 'L1'], ['M0', 'M1', 'N1'], ['O0', 'O1', 'P1'], ['A2', 'A3', 'B3'], ['C2', 'C3', 'D3'], ['E2', 'E3', 'F3'], ['G2', 'G3', 'H3'], ['I2', 'I3', 'J3'], ['K2', 'K3', 'L3'], ['M2', 'M3', 'N3'], ['O2', 'O3', 'P3'], ['A4', 'A5', 'B5'], ['C4', 'C5', 'D5'], ['E4', 'E5', 'F5'], ['G4', 'G5', 'H5'], ['I4', 'I5', 'J5'], ['K4', 'K5', 'L5'], ['M4', 'M5', 'N5'], ['O4', 'O5', 'P5'], ['A6', 'A7', 'B7'], ['C6', 'C7', 'D7'], ['E6', 'E7', 'F7'], ['G6', 'G7', 'H7'], ['I6', 'I7', 'J7'], ['K6', 'K7', 'L7'], ['M6', 'M7', 'N7'], ['O6', 'O7', 'P7'], ['A8', 'A9', 'B9'], ['C8', 'C9', 'D9'], ['E8', 'E9', 'F9'], ['G8', 'G9', 'H9']]
        self.assertEqual(expected_wells, wells)


    def test_create_run_tepmlate_ok(self):
        barcodes = [TubeFactory() for x in range(48)]
        #run_pk = create_run_with_barcodes(barcodes=barcodes, run_method=RUN_METHOD__SALIVECLEAR)
        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__DUPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(len(barcodes)*len(RUN_METHOD_TARGETS__SALIVECLEAR)*2, len(template_wells))

        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(len(barcodes)*len(RUN_METHOD_TARGETS__SALIVECLEAR)*3, len(template_wells))


    def test_create_run_tepmlate_err(self):
        '''
        Barcode count and chosen replication exceeds the 384 well count
        '''
        barcodes = [TubeFactory() for x in range(48*3)]

        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(None, template_wells)
