from __future__ import annotations

from fastmsa.domain import Aggregate

from smartcloset.domain.models import Clothing


class Basket(Aggregate[Clothing]):
    def __init__(self, maker: str, items: list[Clothing], version_number: int = 0):
        self.maker = maker
        self.items = items
        self.version_number = version_number
