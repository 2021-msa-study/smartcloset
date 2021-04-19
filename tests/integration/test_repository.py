# pylint: disable=protected-access
from smartcloset.domain.aggregates import Maker
from smartcloset.domain.models import Closet, MyClothings, Clothing, Partition

from datetime import datetime

from sqlalchemy.orm import Session

from fastmsa.repository import SqlAlchemyRepository

# from tests.app.domain.models import Batch, OrderLine

# from tests.integration import (
#     insert_allocation,
#     insert_batch,
#     insert_order_line,
#     insert_product,
# )


def test_repository_can_save_a_clothing(session: Session) -> None:

    now = datetime.now()
    clothing = Clothing("test-id01", "test-maker01", "test-serial01", now, 5)

    maker = Maker(clothing.maker, [clothing])

    repo = SqlAlchemyRepository(maker, session)
    repo.add(maker)
    session.commit()

    rows = list(session.execute("SELECT id, maker, serial FROM clothing"))

    assert len(rows) == 1
    assert rows == [("test-id01", "test-maker01", "test-serial01")]
