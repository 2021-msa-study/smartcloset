# pylint: disable=protected-access
from smartcloset.domain.aggregates import Basket
from smartcloset.domain.models import Closet, MyClothings, Clothing, Partition

from datetime import datetime

from sqlalchemy.orm import Session

from fastmsa.repository import SqlAlchemyRepository


def test_repository_can_save_a_clothing(session: Session) -> None:

    now = datetime.now()
    clothing = Clothing("test-id01", "test-maker01", "test-serial01", now, 5)

    basket = Basket(clothing.maker, [clothing])

    repo = SqlAlchemyRepository(basket, session)
    repo.add(basket)
    session.commit()

    rows = list(session.execute("SELECT id, maker, serial FROM clothing"))

    assert len(rows) == 1
    assert rows == [("test-id01", "test-maker01", "test-serial01")]
