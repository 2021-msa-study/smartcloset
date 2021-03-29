from typing import Optional, List, Set
from datetime import datetime


class Myclothes:
    def __init__(self):

        self.clothes = set()

    def regist_clothes(self, new_clothes: Clothes):
        self.clothes.add(new_clothes)

    def modify_clothes(self, id: str, modified_clothes: Clothes):
        self.clothes[id].set(modified_clothes)

    def remove_closets(self, id: str):
        self.clothes.remove(id)


class Closet:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name  # 옷장이름
        self.parts = set()  # 옷칸
        self.clothes = set()  # 옷장내 옷

    @property
    def number_of_clothes(self):
        return len(self.Clothes)

    @property
    def number_of_parts(self):
        return len(self.parts)

    def in_parts(self, new_part: Part):
        parts.add(new_part)

    def out_parts(self, id: str):
        self.parts.remove(id)


# x:int,y:int,height:int, width:int
class Part:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.clothes = set()

    def in_clothes(self, new_clotes: Clothes):
        clothes.add(new_clotes)

    def out_clothes(self, id: str):
        self.clothes.remove(id)


class Clothes:
    def __init__(self, id: str, maker: str, serial: str, buydate: datetime,  rating: int):
        self.id = id
        self.maker = maker
        self.serial = serial
        self.buydate = buydate
        self.rating = rating

    def set(self, new_clothes: Clothes):
        self.maker = new_clothes.maker
        self.serial = new_clothes.serial
        self.buydate = new_clothes.buydate
        self.rating = new_clothes.rating
