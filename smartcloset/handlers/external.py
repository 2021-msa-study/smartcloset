"""샘플 이벤트 핸들러."""
from fastmsa.event import on_external_msg

from ..domain.events import SampleEvent


@on_external_msg(SampleEvent)
def handle_external_event(event: SampleEvent):
    """외부 이벤트 메세지를 처리하는  핸들러."""
    print(event.msg)
