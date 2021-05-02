from dataclasses import dataclass, field

from fastmsa.domain import Aggregate

from smartcloset.domain.models import Clothing


@dataclass(unsafe_hash=True)  # type: ignore
class Basket(Aggregate[Clothing]):
    maker: str
    items: list[Clothing] = field(default_factory=list, hash=False)
    version_number: int = field(default=0)
