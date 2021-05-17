from fastmsa.event import on_external_msg

from ..domain.events import SampleEvent


@on_external_msg(SampleEvent)
def handle_external_evnet(event: SampleEvent):
    print(event.msg)
