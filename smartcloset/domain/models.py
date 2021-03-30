from __future__ import annotations
from datetime import datetime


class MyClothing:
    """
    TODO 무슨용도의 클래스인지 설명을 써주세요.
    """

    def __init__(self):
        self.clothings = set[Clothing]()

    def regist_clothing(self, clothing: Clothing):
        self.clothings.add(clothing)

    def modify_clothing(self, id: str, clothing: Clothing):
        # XXX clothing 의 정의가 `set` 이었는데 갑자기 `dict` 처럼 잘못 쓰입니다.
        self.clothings[id].set(clothing)

    def remove_closets(self, id: str):
        # XXX `set[Clothing]` 인데 문자열을 삭제하려고 잘못 시도합니다.
        self.clothings.remove(id)


class Closet:
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

    def out_parts(self, id: str):
        # XXX `set[Part]` 인데 문자열을 삭제하려고 잘못 시도합니다.
        self.parts.remove(id)


class Part:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.clothings = set[Clothing]()

    def in_clothes(self, clothing: Clothing):
        self.clothings.add(clothing)

    def out_clothes(self, clothing: Clothing):
        self.clothings.remove(clothing)


class Clothing:
    """옷 클래스

    참고:
        `Clothes` 나 `Clothing` 이나 단수/복수 구분이 없는 명사지만
        `Clothes` 는 기본 형태가 복수형의 형태라서 컬렉션에 변수를 이름짓기 어렵습니다.
        이런 이유로 `Clothing` 이라는 이름으로 변경했습니다.
        문법적으로는 틀린 표현이지만 `clothings` 로 쓸경우 `set[Clothing]` 같은
        컬렉션 변수로 간주합니다.
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
