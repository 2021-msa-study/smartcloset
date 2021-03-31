from __future__ import annotations
from datetime import datetime


class MyClothing:
    """
    TODO    유저가 가진 모든 옷
            MyClothing 은 유저당 하나씩 생성
            옷장으로 분류되기전 본인이 등록한 모든 옷 개체를 가지고있음
    """

    def __init__(self):
        self.clothings = dict[Clothing]()

    def regist_clothing(self, clothing: Clothing):
        self.clothings.add(clothing)

    def modify_clothing(self, src: Clothing, des: Clothing):

        if src in self.clothings:
            self.clothings.remove(src)
            self.clothings.add(des)

    def remove_clothing(self, clothing: Clothing):

        self.clothings.remove(clothing)


class Closet:
    """
    TODO    옷장- 대분류
        개인의 다양한 대분류에 따라 최대 5개까지 생성가능
        예시2) 옷장 : 옷장("2020년컬렉션, 2021컬렉션") - 옷칸("봄옷, 여름옷, 가을옷, 겨울옷)
    """

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name  # 옷장이름
        self.parts = set[Part]()  # 옷칸
        self.clothings = set[Clothing]()  # 옷장내 옷

    @property
    def number_of_clothes(self):
        return len(self.clothings)

    @property
    def number_of_parts(self):
        return len(self.parts)

    def in_parts(self, part: Part):
        self.parts.add(part)

    def out_parts(self, part: Part):

        self.parts.remove(part)


class Part:
    """
    TODO    옷칸- 소분류
        옷칸"은 "장" 소분류로 옷장당 최대 10칸 생성가능
        예시1) 옷장 : 옷장("봄,여름,가을,겨울") - 옷칸(ex: "상의,하의, 속옷")
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.clothings = set[Clothing]()

    def in_clothes(self, clothing: Clothing):
        self.clothings.add(clothing)

    def out_clothes(self, clothing: Clothing):
        self.clothings.remove(clothing)


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
