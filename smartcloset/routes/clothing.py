"""FastAPI 엔드포인트 라우팅 모듈입니다."""
from datetime import datetime
from smartcloset.domain.models import Clothing, MyClothings

from fastmsa.api import get
from fastmsa.schema import Field, schema_from


@schema_from(Clothing)
class ClothingReadSchema:
    rating: int = Field(..., description="1~5점 사이로 매겨진 평점")


@get("/myclothings", response_model=dict[str, ClothingReadSchema])
def read_myclothings():
    now = datetime.now()

    myclothings = MyClothings()
    clothing01 = Clothing("test-id01", "test-maker01", "test-serial01", now, 5)
    myclothings.add(clothing01)

    now = datetime.now()
    clothing02 = Clothing("test-id02", "test-maker02", "test-serial02", now, 4)
    myclothings.add(clothing02)

    return myclothings.clothings


"""
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

"""