"""ORM 어댑터 모듈"""
from __future__ import annotations

from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper, relationship

from fastmsa.orm import metadata

from smartorder.domain.aggregates import Product
from smartorder.domain.models import Item, User

# Domain 매핑
user = Table(
    "user",
    metadata,
    Column("id", String(255), primary_key=True),
    Column("name", String(255)),
    Column("email", String(255), unique=True),
    extend_existing=True,
)

item = Table(
    "item",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("uuid", String(36), unique=True),
    Column("product_id", ForeignKey("product.id")),
    Column("created", DateTime, nullable=True),
    extend_existing=True,
)

# Aggregate 매핑
product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("version_number", Integer, nullable=False, server_default="0"),
    extend_existing=True,
)

mapper(User, user)
mapper(Item, item)
mapper(Product, product, properties={"items": relationship(Item)})