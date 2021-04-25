from fastmsa.uow import AbstractUnitOfWork

def add(
    ref: str, maker: str, qty: int, AbstractUnitOfWork[Clothings]
) -> None:
    """UOW를 이용해 배치를 추가합니다."""
    with uow:
        clothings = uow.repo.get(maker)

        if not clothings:
            clothings = Clothings(maker, items=[])
            uow.repo.add(clothings)

        clothings.items.append(Clothing(...))
        uow.commit()
