import logging
import csv
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile

from common.data import TubePositionData, TubesBatchData
from .const import FILE_HEADER_DATE, FILE_HEADER_TIME, FILE_HEADER_RACKBARCODE, FILE_HEADER_POSITION, FILE_HEADER_TUBEBARCODE

logger = logging.getLogger(__name__)


def parse_batch_data_from_file(*, full_file):
    if isinstance(full_file, InMemoryUploadedFile):
        import codecs
        reader = csv.DictReader(codecs.iterdecode(full_file, 'utf-8'), delimiter=';')
    else:
        reader = csv.DictReader(full_file, delimiter=';')

    tube_data = []
    for row in reader:
        tube_data.append(row)
    return tube_data

def get_tube_batch_from_tube_data(*, tube_data, batch_type):
    tubes = []
    for idx, tube in enumerate(tube_data):
        tubes.append(TubePositionData(barcode=tube[FILE_HEADER_TUBEBARCODE], position=tube[FILE_HEADER_POSITION]))

    batch_id = ''
    date = ''
    time = ''
    try:
        if len(tubes):
            batch_id = tube_data[0][FILE_HEADER_RACKBARCODE]
            date = tube_data[0][FILE_HEADER_DATE]
            time = tube_data[0][FILE_HEADER_TIME]
    except KeyError as e:
        logger.error(f'Tube data is missing some keys. Cannot create TubesBatchData object.', e)
        return None
    date_time = datetime.strptime(f'{date} {time}', "%m/%d/%Y %I:%M:%S %p")
    title_date = datetime.strptime(f'{date}', "%m/%d/%Y").strftime('%A %d')
    return TubesBatchData(batch_type=batch_type, batch_id=batch_id, timestamp=date_time.isoformat(), tubes=tubes, title=f'{title_date} batch')