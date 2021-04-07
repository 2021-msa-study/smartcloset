from datetime import datetime

import pytest

from smartcloset.domain.models import Closet, MyClothings, Clothing, Partition


@pytest.fixture
def myclothings():

    myclothings = MyClothings()
    now = datetime.now()
    clothing01 = Clothing("test-id01", "test-maker01", "test-serial01", now, 5)
    myclothings.add_clothing(clothing01)

    now = datetime.now()
    clothing02 = Clothing("test-id02", "test-maker02", "test-serial02", now, 4)
    myclothings.add_clothing(clothing02)

    return myclothings


def test_regist_clothes(myclothings: MyClothings):
    assert len(myclothings.clothings) == 2


def test_add_clothing_to_closet(myclothings: MyClothings):
    """
    +------------+------------+
    |            |            |
    |    (0,0)   |    (1,0)   |
    +------------|------------+
    |    (0,1)   |    (1,1)   |
    |            |            |
    +------------+------------+
    """
    closet = Closet("closet-1", "test-closet")
    part0_0 = Partition(0, 0)
    part0_1 = Partition(0, 1)
    part1_0 = Partition(1, 0)
    part1_1 = Partition(1, 1)

    closet.add_partition(part0_0)
    closet.add_partition(part1_0)
    closet.add_partition(part0_1)
    closet.add_partition(part1_1)
    assert 4 == len(closet.partitions)

    myclothings.allocate(part0_0, "test-id01")
    assert 1 == closet.number_of_clothes

    myclothings.allocate(part0_1, "test-id02")
    assert 2 == closet.number_of_clothes

    myclothings.deallocate(part0_0, "test-id01")
    assert 1 == closet.number_of_clothes


def test_modify_clothes(myclothings: MyClothings):
    myclothings.update_clothing(
        "test-id01", maker="test-maker03", serial="test-serial03"
    )
    assert myclothings.clothings["test-id01"].maker == "test-maker03"
    assert myclothings.clothings["test-id01"].serial == "test-serial03"


def test_remove_clothes(myclothings: MyClothings):
    myclothings.remove_clothing("test-id01")
    assert 1 == len(myclothings.clothings)
