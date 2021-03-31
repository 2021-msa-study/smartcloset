from datetime import datetime

from smartcloset.domain.models import MyClothing, Clothing


def test_regist_clothes():
    now = datetime.now()

    myclothes = MyClothing()
    clothing = Clothing("test-id", "test-maker", "test-serial", now, 5)

    myclothes.regist_clothing(clothing)

    assert len(myclothes.clothings) == 1


def test_modify_clothes():
    raise NotImplementedError


def test_remove_clothes():
    raise NotImplementedError
