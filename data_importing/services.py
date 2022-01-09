import csv
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile

from common.data import TubePositionData, TubesBatchData


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
        print(idx, tube)
        tubes.append(TubePositionData(barcode=tube['Tube barcode'], position=tube['Position']))

    batch_id = ''
    date = ''
    time = ''
    try:
        if len(tubes):
            batch_id = tube_data[0]['Rack barcode']
            date = tube_data[0]['Date']
            time = tube_data[0]['Time']
    except KeyError as e:
        return None
    date_time = datetime.strptime(f'{date} {time}', "%m/%d/%Y %I:%M:%S %p")
    title_date = datetime.strptime(f'{date}', "%m/%d/%Y").strftime('%A %d')
    return TubesBatchData(batch_type=batch_type, batch_id=batch_id, timestamp=date_time.isoformat(), tubes=tubes, title=f'{title_date} batch')