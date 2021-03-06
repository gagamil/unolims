from .const import RUN_REPLICATION__DUPLICATE, RUN_REPLICATION__DUPLICATE__PATTERN, \
    RUN_REPLICATION__TRIPLICATE, RUN_REPLICATION__TRIPLICATE__PATTERN, \
    RUN_WELLPLATE__384, RUN_WELLPLATE__384_LAYOUT, RUN_WELLPLATE__CONFIGS, ALPHABET


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


def get_wells_with_pattern_mask(*, pattern_mask, well_count, row_max_idx, col_max_idx):
    curr_row_offset = 0
    row_offset_step = len(pattern_mask)
    curr_col_offset = 0
    col_offset_step = 2

    wells = []
    for idx in range(well_count):
        wells.append(get_wells(row_start=curr_row_offset, col_start=curr_col_offset, pattern_mask=pattern_mask))
        #   calculate next position
        if curr_row_offset + row_offset_step +1 > row_max_idx or curr_row_offset + row_offset_step +1 > len(ALPHABET):
            # need to change colums - let's see if we can
            if curr_col_offset + col_offset_step > col_max_idx:
                return []
            curr_row_offset = 0
            curr_col_offset += col_offset_step
        else:
            curr_row_offset += row_offset_step
    return wells


def populate_wells_with_sample(*, targets, well_group, barcode):
    result = []
    for well in well_group:
        for target in targets:
            result.append({'well':well, 'sample':barcode, 'target':target})
    return result

def get_plate_max_counts(*, well_plate_type):
    if well_plate_type == RUN_WELLPLATE__384:
        # define max row and col idx
        config = next(item for item in RUN_WELLPLATE__CONFIGS if item["name"] == RUN_WELLPLATE__384)
        layout = config['layout']
        well_count = layout['well_count']
        rows = layout['rows']
        row_max_idx = ALPHABET.index(rows[1])
        cols = layout['cols']
        col_max_idx = cols[1]
        return row_max_idx, col_max_idx, well_count

def create_well_plate_template(*, barcodes, replication, targets, well_plate=RUN_WELLPLATE__384):
    '''
    Check the well capacity fits the barcode count * replication
    '''
    wells = None
    
    row_max_idx, col_max_idx, well_count = get_plate_max_counts(well_plate_type=well_plate)

    if replication == RUN_REPLICATION__DUPLICATE:
        if well_count < len(barcodes)*2:
            return None
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__DUPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx, col_max_idx=col_max_idx)
    elif replication == RUN_REPLICATION__TRIPLICATE:
        if well_count < len(barcodes)*3:
            return None
        wells = get_wells_with_pattern_mask(pattern_mask=RUN_REPLICATION__TRIPLICATE__PATTERN, well_count=len(barcodes), row_max_idx=row_max_idx, col_max_idx=col_max_idx)

    final_wells = []
    for idx, well_group in enumerate(wells):
        final_wells.extend(populate_wells_with_sample(targets=targets, well_group=well_group, barcode=barcodes[idx]))
    return final_wells