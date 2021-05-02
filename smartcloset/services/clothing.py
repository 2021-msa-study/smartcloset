from datetime import datetime

from fastmsa.uow import AbstractUnitOfWork

from ..domain.aggregates import Basket
from ..domain.models import Clothing


def add(
    id: str,
    maker: str,
    serial: str,
    buydate: datetime,
    rating: int,
    uow: AbstractUnitOfWork[Basket],
):
    """UOW를 이용해 배치를 추가합니다."""
    with uow:
        basket = uow.repo.get(maker)

        if not basket:
            basket = Basket(maker, items=[])
            uow.repo.add(basket)

        basket.items.append(Clothing(id, maker, serial, buydate, rating))
        uow.commit()
