from django.test import TestCase

from tubes.tests.factories import TubeFactory
from .models import Run
from .const import RUN_REPLICATION__DUPLICATE, RUN_REPLICATION__DUPLICATE__PATTERN, \
    RUN_REPLICATION__TRIPLICATE, RUN_REPLICATION__TRIPLICATE__PATTERN, \
    RUN_WELLPLATE__384, RUN_WELLPLATE__384_LAYOUT, RUN_WELLPLATE__CONFIGS, ALPHABET, RUN_METHOD_TARGETS__SALIVECLEAR
from .services import create_well_plate_template,  get_wells_with_pattern_mask, get_plate_max_counts


# def create_run_with_barcodes(*, barcodes, run_method):
#     Run.objects.create(barcodes=barcodes,run_characteristics, well_template, run_file)
class RunCreateTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_build_wells(self):
        row_max_idx, col_max_idx, well_count = get_plate_max_counts(well_plate_type=RUN_WELLPLATE__384)

        barcodes = [TubeFactory() for x in range(48*4)]
        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__DUPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__DUPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx, col_max_idx=col_max_idx)
        expected_wells = [['A0', 'A1'], ['B0', 'B1'], ['C0', 'C1'], ['D0', 'D1'], ['E0', 'E1'], ['F0', 'F1'], ['G0', 'G1'], ['H0', 'H1'], ['I0', 'I1'], ['J0', 'J1'], ['K0', 'K1'], ['L0', 'L1'], ['M0', 'M1'], ['N0', 'N1'], ['O0', 'O1'], ['A2', 'A3'], ['B2', 'B3'], ['C2', 'C3'], ['D2', 'D3'], ['E2', 'E3'], ['F2', 'F3'], ['G2', 'G3'], ['H2', 'H3'], ['I2', 'I3'], ['J2', 'J3'], ['K2', 'K3'], ['L2', 'L3'], ['M2', 'M3'], ['N2', 'N3'], ['O2', 'O3'], ['A4', 'A5'], ['B4', 'B5'], ['C4', 'C5'], ['D4', 'D5'], ['E4', 'E5'], ['F4', 'F5'], ['G4', 'G5'], ['H4', 'H5'], ['I4', 'I5'], ['J4', 'J5'], ['K4', 'K5'], ['L4', 'L5'], ['M4', 'M5'], ['N4', 'N5'], ['O4', 'O5'], ['A6', 'A7'], ['B6', 'B7'], ['C6', 'C7'], ['D6', 'D7'], ['E6', 'E7'], ['F6', 'F7'], ['G6', 'G7'], ['H6', 'H7'], ['I6', 'I7'], ['J6', 'J7'], ['K6', 'K7'], ['L6', 'L7'], ['M6', 'M7'], ['N6', 'N7'], ['O6', 'O7'], ['A8', 'A9'], ['B8', 'B9'], ['C8', 'C9'], ['D8', 'D9'], ['E8', 'E9'], ['F8', 'F9'], ['G8', 'G9'], ['H8', 'H9'], ['I8', 'I9'], ['J8', 'J9'], ['K8', 'K9'], ['L8', 'L9'], ['M8', 'M9'], ['N8', 'N9'], ['O8', 'O9'], ['A10', 'A11'], ['B10', 'B11'], ['C10', 'C11'], ['D10', 'D11'], ['E10', 'E11'], ['F10', 'F11'], ['G10', 'G11'], ['H10', 'H11'], ['I10', 'I11'], ['J10', 'J11'], ['K10', 'K11'], ['L10', 'L11'], ['M10', 'M11'], ['N10', 'N11'], ['O10', 'O11'], ['A12', 'A13'], ['B12', 'B13'], ['C12', 'C13'], ['D12', 'D13'], ['E12', 'E13'], ['F12', 'F13'], ['G12', 'G13'], ['H12', 'H13'], ['I12', 'I13'], ['J12', 'J13'], ['K12', 'K13'], ['L12', 'L13'], ['M12', 'M13'], ['N12', 'N13'], ['O12', 'O13'], ['A14', 'A15'], ['B14', 'B15'], ['C14', 'C15'], ['D14', 'D15'], ['E14', 'E15'], ['F14', 'F15'], ['G14', 'G15'], ['H14', 'H15'], ['I14', 'I15'], ['J14', 'J15'], ['K14', 'K15'], ['L14', 'L15'], ['M14', 'M15'], ['N14', 'N15'], ['O14', 'O15'], ['A16', 'A17'], ['B16', 'B17'], ['C16', 'C17'], ['D16', 'D17'], ['E16', 'E17'], ['F16', 'F17'], ['G16', 'G17'], ['H16', 'H17'], ['I16', 'I17'], ['J16', 'J17'], ['K16', 'K17'], ['L16', 'L17'], ['M16', 'M17'], ['N16', 'N17'], ['O16', 'O17'], ['A18', 'A19'], ['B18', 'B19'], ['C18', 'C19'], ['D18', 'D19'], ['E18', 'E19'], ['F18', 'F19'], ['G18', 'G19'], ['H18', 'H19'], ['I18', 'I19'], ['J18', 'J19'], ['K18', 'K19'], ['L18', 'L19'], ['M18', 'M19'], ['N18', 'N19'], ['O18', 'O19'], ['A20', 'A21'], ['B20', 'B21'], ['C20', 'C21'], ['D20', 'D21'], ['E20', 'E21'], ['F20', 'F21'], ['G20', 'G21'], ['H20', 'H21'], ['I20', 'I21'], ['J20', 'J21'], ['K20', 'K21'], ['L20', 'L21'], ['M20', 'M21'], ['N20', 'N21'], ['O20', 'O21'], ['A22', 'A23'], ['B22', 'B23'], ['C22', 'C23'], ['D22', 'D23'], ['E22', 'E23'], ['F22', 'F23'], ['G22', 'G23'], ['H22', 'H23'], ['I22', 'I23'], ['J22', 'J23'], ['K22', 'K23'], ['L22', 'L23'], ['M22', 'M23'], ['N22', 'N23'], ['O22', 'O23'], ['A24', 'A25'], ['B24', 'B25'], ['C24', 'C25'], ['D24', 'D25'], ['E24', 'E25'], ['F24', 'F25'], ['G24', 'G25'], ['H24', 'H25'], ['I24', 'I25'], ['J24', 'J25'], ['K24', 'K25'], ['L24', 'L25']]
        self.assertEqual(expected_wells, wells)

        barcodes = [TubeFactory() for x in range(48*2)]
        # wells = create_well_plate_template(barcodes=[bc.tube_id for bc in barcodes], replication=RUN_REPLICATION__TRIPLICATE, targets=RUN_METHOD_TARGETS__SALIVECLEAR)
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__TRIPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx, col_max_idx=col_max_idx)
        expected_wells = [['A0', 'A1', 'B1'], ['C0', 'C1', 'D1'], ['E0', 'E1', 'F1'], ['G0', 'G1', 'H1'], ['I0', 'I1', 'J1'], ['K0', 'K1', 'L1'], ['M0', 'M1', 'N1'], ['O0', 'O1', 'P1'], ['A2', 'A3', 'B3'], ['C2', 'C3', 'D3'], ['E2', 'E3', 'F3'], ['G2', 'G3', 'H3'], ['I2', 'I3', 'J3'], ['K2', 'K3', 'L3'], ['M2', 'M3', 'N3'], ['O2', 'O3', 'P3'], ['A4', 'A5', 'B5'], ['C4', 'C5', 'D5'], ['E4', 'E5', 'F5'], ['G4', 'G5', 'H5'], ['I4', 'I5', 'J5'], ['K4', 'K5', 'L5'], ['M4', 'M5', 'N5'], ['O4', 'O5', 'P5'], ['A6', 'A7', 'B7'], ['C6', 'C7', 'D7'], ['E6', 'E7', 'F7'], ['G6', 'G7', 'H7'], ['I6', 'I7', 'J7'], ['K6', 'K7', 'L7'], ['M6', 'M7', 'N7'], ['O6', 'O7', 'P7'], ['A8', 'A9', 'B9'], ['C8', 'C9', 'D9'], ['E8', 'E9', 'F9'], ['G8', 'G9', 'H9'], ['I8', 'I9', 'J9'], ['K8', 'K9', 'L9'], ['M8', 'M9', 'N9'], ['O8', 'O9', 'P9'], ['A10', 'A11', 'B11'], ['C10', 'C11', 'D11'], ['E10', 'E11', 'F11'], ['G10', 'G11', 'H11'], ['I10', 'I11', 'J11'], ['K10', 'K11', 'L11'], ['M10', 'M11', 'N11'], ['O10', 'O11', 'P11'], ['A12', 'A13', 'B13'], ['C12', 'C13', 'D13'], ['E12', 'E13', 'F13'], ['G12', 'G13', 'H13'], ['I12', 'I13', 'J13'], ['K12', 'K13', 'L13'], ['M12', 'M13', 'N13'], ['O12', 'O13', 'P13'], ['A14', 'A15', 'B15'], ['C14', 'C15', 'D15'], ['E14', 'E15', 'F15'], ['G14', 'G15', 'H15'], ['I14', 'I15', 'J15'], ['K14', 'K15', 'L15'], ['M14', 'M15', 'N15'], ['O14', 'O15', 'P15'], ['A16', 'A17', 'B17'], ['C16', 'C17', 'D17'], ['E16', 'E17', 'F17'], ['G16', 'G17', 'H17'], ['I16', 'I17', 'J17'], ['K16', 'K17', 'L17'], ['M16', 'M17', 'N17'], ['O16', 'O17', 'P17'], ['A18', 'A19', 'B19'], ['C18', 'C19', 'D19'], ['E18', 'E19', 'F19'], ['G18', 'G19', 'H19'], ['I18', 'I19', 'J19'], ['K18', 'K19', 'L19'], ['M18', 'M19', 'N19'], ['O18', 'O19', 'P19'], ['A20', 'A21', 'B21'], ['C20', 'C21', 'D21'], ['E20', 'E21', 'F21'], ['G20', 'G21', 'H21'], ['I20', 'I21', 'J21'], ['K20', 'K21', 'L21'], ['M20', 'M21', 'N21'], ['O20', 'O21', 'P21'], ['A22', 'A23', 'B23'], ['C22', 'C23', 'D23'], ['E22', 'E23', 'F23'], ['G22', 'G23', 'H23'], ['I22', 'I23', 'J23'], ['K22', 'K23', 'L23'], ['M22', 'M23', 'N23'], ['O22', 'O23', 'P23']]
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
