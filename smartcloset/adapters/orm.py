"""ORM 어댑터 모듈"""
from __future__ import annotations

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    String,
)
from sqlalchemy.orm import (
    mapper,
)

from smartcloset.domain.models import Clothing


def init_mappers(metadata: MetaData) -> MetaData:
    """도메인 객체들을 SqlAlchemy ORM 매퍼에 등록합니다."""

    clothing = Table(
        "clothing",
        metadata,
        Column("id", String(255), primary_key=True, autoincrement=True),
        extend_existing=True,
    )

    mapper(
        Clothing,
        clothing,
    )

    return metadata
