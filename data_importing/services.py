import csv
from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class BatchTubeData:
    barcode: str
    position: str
    
@dataclass
class BatchImportData:
    '''
    - batch_id: equals rack ID
    - timestamp: ISO str
    '''
    batch_id: str
    timestamp: str
    tubes: List[BatchTubeData]


def parse_batch_data_from_file(*, full_file):
    reader = csv.DictReader(full_file, delimiter=';')
    tube_data = []
    for row in reader:
        tube_data.append(row)
        # print(row['Number'], row['Rack barcode'], row['Tube barcode'], row['Date'], row['Time'], row['Position'])
    return tube_data

def get_tube_batch_from_tube_data(*, tube_data):
    tubes = []
    for idx, tube in enumerate(tube_data):
        print(idx, tube)
        tubes.append(BatchTubeData(barcode=tube['Tube barcode'], position=tube['Position']))

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
    return BatchImportData(batch_id=batch_id, timestamp=date_time.isoformat(), tubes=tubes)