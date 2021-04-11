"""FastAPI 엔드포인트 라우팅 모듈입니다."""
from __future__ import annotations
from datetime import datetime
from typing import Optional

from fastmsa.uow import SqlAlchemyUnitOfWork
from fastmsa.api import post, delete, BaseModel

from smartcloset.domain.models import Clothing
from smartcloset.domain.aggregates import Clothings


class ClothingAdd(BaseModel):
    id: str
    maker: str
    serial: str


@post("/clothings")
def add_clothing(req: ClothingAdd):
    with SqlAlchemyUnitOfWork(Clothigns) as uow:
        product = uow.repo.get(req.sku)
        if product:
            line = OrderLine(req.orderid, req.sku, req.qty)
            batchref = product.allocate(line)
            uow.commit()

        return {"batchref": batchref}
