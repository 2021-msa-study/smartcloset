from dataclasses import dataclass

from fastmsa.core import Command
from fastmsa.event import on_external_msg

from ..domain.events import SampleEvent


@dataclass
class CreateOrder(Command):
    product_id: str


@on_external_msg(SampleEvent)
def handle_external_evnet(event: SampleEvent):
    print(event.msg)
