from datetime import datetime

import uuid

from smartorder.domain.models import Item, User
from smartorder.domain.aggregates import Product


def test_create_models():
    now = datetime.now()

    product_id = "test-product"
    product = Product(product_id, [])
    item = Item(1, uuid.uuid4(), product_id, now)