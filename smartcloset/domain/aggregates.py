from __future__ import annotations
from dataclasses import dataclass, field

from fastmsa.domain import Aggregate

from smartcloset.domain.models import Clothing


@dataclass
class Basket(Aggregate[Clothing]):
    maker: str
    items: list[Clothing] = field(default_factory=list)
    version_number: int = field(default=0)
