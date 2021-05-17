from fastmsa.test.unit import FakeRepository

from smartorder.domain.aggregates import Product

def test_fake_repo():
    repo = FakeRepository[Product]('id', [])