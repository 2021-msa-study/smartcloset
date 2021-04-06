from datetime import datetime

import pytest

from smartcloset.domain.models import Closet, MyClothings, Clothing, Partition


@pytest.fixture
def myclothings():
    now = datetime.now()

    myclothings = MyClothings()
    clothing = Clothing("test-id", "test-maker", "test-serial", now, 5)

    myclothings.add_clothing(clothing)
    return myclothings


def test_regist_clothes(myclothings: MyClothings):
    assert len(myclothings.clothings) == 1


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

    myclothings.allocate(part0_0, "test-id")
    assert 1 == closet.number_of_clothes


def test_modify_clothes(myclothings: MyClothings):
    myclothings.update_clothing("test-id", maker="test-maker2", serial="test-serial2")
    assert myclothings.clothings["test-id"].maker == "test-maker2"
    assert myclothings.clothings["test-id"].serial == "test-serial2"


def test_remove_clothes(myclothings: MyClothings):
    myclothings.remove_clothing("test-id")
    assert 0 == len(myclothings.clothings)
