from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json


@dataclass
class Tube:
    id: str
    barcode: str


@dataclass
class TubePositionData:
    barcode: str
    position: str

@dataclass_json
@dataclass
class TubesBatchData:
    '''
    - batch_id: equals rack ID
    - timestamp: ISO str
    '''
    batch_type: str
    batch_id: str
    timestamp: str
    tubes: List[TubePositionData]
    title: str = ''

@dataclass
class RunData:
    id: str
    title: str
    tubes: List[Tube]
    run_characteristics: object