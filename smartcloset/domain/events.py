"""사용자 이벤트 정의."""
from dataclasses import dataclass

from fastmsa.core import Event

from smartcloset.domain.models import MyClothings, Clothing, Partition


@dataclass
class SampleEvent(Event):
    "샘플 이벤트"
    msg: str


@dataclass
class Added(Event):
    "옷 추가"
    myClothings: MyClothings
    clothing: Clothing


@dataclass
class Removed(Event):
    "옷 삭제"
    myClothings: MyClothings
    clothing_id: str


@dataclass
class Allocated(Event):
    "옷장 파티션에 옷 할당"
    myClothings: MyClothings
    partition: Partition
    clothing_id: str


@dataclass
class Deallocated(Event):
    "옷장 파티션에 옷 해제"
    myClothings: MyClothings
    partition: Partition
    clothing_id: str
