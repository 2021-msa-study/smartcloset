from __future__ import annotations
from datetime import datetime
from typing import Optional


class MyClothings:
    """유저가 가진 모든 옷.

    MyClothing 은 유저당 하나씩 생성
    옷장으로 분류되기전 본인이 등록한 모든 옷 개체를 가지고있음
    """

    def __init__(self):
        self.clothings = dict[str, Clothing]()

    def add_clothing(self, clothing: Clothing):
        assert clothing.id not in self.clothings
        self.clothings[clothing.id] = clothing

    def update_clothing(self, id: str, **kwargs):  # type: ignore
        assert id in self.clothings
        clothing = self.clothings[id]

        for key, value in kwargs.items():  # type: ignore
            setattr(clothing, key, value)

    def remove_clothing(self, id: str):
        assert id in self.clothings
        del self.clothings[id]

    def allocate(self, partition: Partition, clothing_id: str):
        assert clothing_id in self.clothings
        clothing = self.clothings[clothing_id]
        assert partition.closet
        assert clothing_id not in partition.closet.clothings

        partition.closet.alloc_clothing(clothing)


class Closet:
    """옷장- 대분류.

    개인의 다양한 대분류에 따라 최대 5개까지 생성가능
    예시2) 옷장 : 옷장("2020년컬렉션, 2021컬렉션") - 옷칸("봄옷, 여름옷, 가을옷, 겨울옷)
    """

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name  # 옷장이름
        self.partitions = set[Partition]()  # 옷칸
        self.clothings = set[Clothing]()  # 옷장내 옷

    @property
    def number_of_clothes(self):
        return len(self.clothings)

    @property
    def number_of_parts(self):
        return len(self.partitions)

    def add_partition(self, partition: Partition):
        self.partitions.add(partition)
        partition.closet = self

    def remove_partition(self, partition: Partition):
        self.partitions.remove(partition)
        partition.closet = self

    def alloc_clothing(self, clothing: Clothing):
        self.clothings.add(clothing)

    def dealloc_clothing(self, clothing: Clothing):
        self.clothings.remove(clothing)


class Partition:
    """
    TODO    옷칸- 소분류
        옷칸"은 "장" 소분류로 옷장당 최대 10칸 생성가능
        예시1) 옷장 : 옷장("봄,여름,가을,겨울") - 옷칸(ex: "상의,하의, 속옷")
    """

    def __init__(self, x: int, y: int, closet: Optional[Closet] = None):
        self.x = x
        self.y = y
        self.closet = closet


class Clothing:
    """
    TODO 옷
    동일 옷 entity는  n개의 옷장에  속할수 있음.
    같은 옷장안에서 동일 옷 entity는 1개의 옷칸에만 속할 수있음
    """

    def __init__(
        self, id: str, maker: str, serial: str, buydate: datetime, rating: int
    ):
        self.id = id
        self.maker = maker
        self.serial = serial
        self.buydate = buydate
        self.rating = rating

    def set(self, clothing: Clothing):
        self.maker = clothing.maker
        self.serial = clothing.serial
        self.buydate = clothing.buydate
        self.rating = clothing.rating
