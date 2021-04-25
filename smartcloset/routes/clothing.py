"""FastAPI 엔드포인트 라우팅 모듈입니다."""
from datetime import datetime

from fastmsa.api import get
from fastmsa.uow import SqlAlchemyUnitOfWork
from fastmsa.schema import Field, schema_from, BaseModel

from ..domain.models import Clothing, MyClothings
from ..domain.aggregates import Basket


@schema_from(Clothing)
class ClothingReadSchema:
    rating: int = Field(..., description="1~5점 사이로 매겨진 평점")


class BasketReadSchema(BaseModel):
    maker: str
    items: list[ClothingReadSchema] = Field(default_factory=list)
    version_number: int = Field(default=0)

    class Config:
        orm_mode = True


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


@get("/baskets/test", response_model=list[BasketReadSchema])
def read_test_baskets():
    with SqlAlchemyUnitOfWork(Basket) as uow:
        baskets = uow.repo.all()
        print(baskets)
        return baskets
    ...
