"""ORM 어댑터 모듈"""
from __future__ import annotations

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
)
from sqlalchemy.orm import (
    mapper,
    relationship,
)
from sqlalchemy.sql.sqltypes import DateTime, Integer

from smartcloset.domain.models import Clothing
from smartcloset.domain.aggregates import Maker


def init_mappers(metadata: MetaData) -> MetaData:
    """도메인 객체들을 SqlAlchemy ORM 매퍼에 등록합니다."""

    clothing = Table(
        "clothing",
        metadata,
        Column("id", String(255), primary_key=True),
        Column("maker", String(255), ForeignKey("maker.maker")),
        Column("serial", String(255)),
        Column("buydate", DateTime),
        Column("rating", Integer),
        extend_existing=True,
    )

    mapper(
        Clothing,
        clothing,
    )

    # Aggregate 매핑 추가
    maker = Table(
        "maker",
        metadata,
        Column("maker", String(255), primary_key=True),
        Column("version_number", Integer, nullable=False, server_default="0"),
        extend_existing=True,
    )

    mapper(Maker, maker, properties={"items": relationship(Clothing)})

    return metadata
