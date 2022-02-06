from .const import RUN_REPLICATION__DUPLICATE, RUN_REPLICATION__DUPLICATE__PATTERN, \
    RUN_REPLICATION__TRIPLICATE, RUN_REPLICATION__TRIPLICATE__PATTERN, \
    RUN_WELLPLATE__384, RUN_WELLPLATE__384_LAYOUT, ALPHABET


def get_wells(*, row_start, col_start, pattern_mask):
    '''
    It should be guaranteed by the caller that row_start and col_start + the offsets 
    in the pattern do not lead to overflow.
    '''
    wells = []
    row_offset = 0
    col_offset = 0
    for row in pattern_mask:
        for cell in row:
            if cell == 'X':
                curr_row = ALPHABET[row_start + row_offset]
                curr_col = col_start + col_offset
                wells.append(f'{curr_row}{curr_col}')
            col_offset += 1
        row_offset += 1
        col_offset = 0
    return wells


def get_wells_with_pattern_mask(*, pattern_mask, well_count):
    curr_row_offset = 0
    row_offset_step = len(pattern_mask)
    curr_col_offset = 0
    col_offset_step = 2

    wells = []
    for idx in range(well_count):
        wells.append(get_wells(row_start=curr_row_offset, col_start=curr_col_offset, pattern_mask=pattern_mask))
        #   calculate next position
        if curr_row_offset + row_offset_step +1 > len(ALPHABET):
            curr_row_offset = 0
            curr_col_offset += col_offset_step
        else:
            curr_row_offset += row_offset_step
    return wells


def create_well_plate_template(*, barcodes, replication, targets, well_plate=RUN_WELLPLATE__384):
    wells = None
    if well_plate == RUN_WELLPLATE__384:
        if replication == RUN_REPLICATION__DUPLICATE:
            wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__DUPLICATE__PATTERN, well_count=len(barcodes))
        elif replication == RUN_REPLICATION__TRIPLICATE:
            wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__TRIPLICATE__PATTERN, well_count=len(barcodes))

    if wells:
        pass
    return wells