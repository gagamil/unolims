from django.test import TestCase

from tubes.tests.factories import TubeFactory
from .models import Run
from .const import RUN_METHOD__SALIVECLEAR, RUN_METHOD_TARGETS__SALIVECLEAR, RUN_REPLICATION__DUPLICATE, RUN_REPLICATION__DUPLICATE__PATTERN, \
    RUN_REPLICATION__TRIPLICATE, RUN_REPLICATION__TRIPLICATE__PATTERN
from .services import create_well_plate_template,  get_wells_with_pattern_mask


# def create_run_with_barcodes(*, barcodes, run_method):
#     Run.objects.create(barcodes=barcodes,run_characteristics, well_template, run_file)
class RunCreateTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_build_wells(self):
        barcodes = [TubeFactory() for x in range(36)]
        # run_pk = create_run_with_barcodes(barcodes=barcodes, run_method=RUN_METHOD__SALIVECLEAR)
        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__DUPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__DUPLICATE__PATTERN, well_count=len(barcodes))
        expected_wells = [['A0', 'A1'], ['B0', 'B1'], ['C0', 'C1'], ['D0', 'D1'], ['E0', 'E1'], ['F0', 'F1'], ['G0', 'G1'], ['H0', 'H1'], ['I0', 'I1'], ['J0', 'J1'], ['K0', 'K1'], ['L0', 'L1'], ['M0', 'M1'], ['N0', 'N1'], ['O0', 'O1'], ['P0', 'P1'], ['Q0', 'Q1'], ['R0', 'R1'], ['S0', 'S1'], ['T0', 'T1'], ['U0', 'U1'], ['V0', 'V1'], ['W0', 'W1'], ['X0', 'X1'], ['Y0', 'Y1'], ['Z0', 'Z1'], ['A2', 'A3'], ['B2', 'B3'], ['C2', 'C3'], ['D2', 'D3'], ['E2', 'E3'], ['F2', 'F3'], ['G2', 'G3'], ['H2', 'H3'], ['I2', 'I3'], ['J2', 'J3']]
        self.assertEqual(expected_wells, wells)

        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__TRIPLICATE__PATTERN, well_count=len(barcodes))
        expected_wells = [['A0', 'A1', 'B1'], ['C0', 'C1', 'D1'], ['E0', 'E1', 'F1'], ['G0', 'G1', 'H1'], ['I0', 'I1', 'J1'], ['K0', 'K1', 'L1'], ['M0', 'M1', 'N1'], ['O0', 'O1', 'P1'], ['Q0', 'Q1', 'R1'], ['S0', 'S1', 'T1'], ['U0', 'U1', 'V1'], ['W0', 'W1', 'X1'], ['Y0', 'Y1', 'Z1'], ['A2', 'A3', 'B3'], ['C2', 'C3', 'D3'], ['E2', 'E3', 'F3'], ['G2', 'G3', 'H3'], ['I2', 'I3', 'J3'], ['K2', 'K3', 'L3'], ['M2', 'M3', 'N3'], ['O2', 'O3', 'P3'], ['Q2', 'Q3', 'R3'], ['S2', 'S3', 'T3'], ['U2', 'U3', 'V3'], ['W2', 'W3', 'X3'], ['Y2', 'Y3', 'Z3'], ['A4', 'A5', 'B5'], ['C4', 'C5', 'D5'], ['E4', 'E5', 'F5'], ['G4', 'G5', 'H5'], ['I4', 'I5', 'J5'], ['K4', 'K5', 'L5'], ['M4', 'M5', 'N5'], ['O4', 'O5', 'P5'], ['Q4', 'Q5', 'R5'], ['S4', 'S5', 'T5']]
        self.assertEqual(expected_wells, wells)


    def test_create_run_tepmlate_ok(self):
        barcodes = [TubeFactory() for x in range(48)]
        #run_pk = create_run_with_barcodes(barcodes=barcodes, run_method=RUN_METHOD__SALIVECLEAR)
        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__DUPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(len(barcodes)*len(RUN_METHOD_TARGETS__SALIVECLEAR)*2, len(template_wells))

        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(len(barcodes)*len(RUN_METHOD_TARGETS__SALIVECLEAR)*3, len(template_wells))
        
    
        print(len(template_wells), len(barcodes)*3)

    def test_create_run_tepmlate_err(self):
        '''
        Barcode count and chosen replication exceeds the 384 well count
        '''
        barcodes = [TubeFactory() for x in range(48*3)]

        template_wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        self.assertEqual(None, template_wells)
