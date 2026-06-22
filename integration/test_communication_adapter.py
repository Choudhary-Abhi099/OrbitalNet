from integration.event_bus import EventBus

from integration.communication_adapter import (
    CommunicationAdapter
)

from integration.events import (
    LINK_DOWN,
    LINK_RECOVERED
)

from integration.event_handlers import (
    link_down_handler,
    link_recovered_handler
)

event_bus = EventBus()

event_bus.subscribe(
    LINK_DOWN,
    link_down_handler
)

event_bus.subscribe(
    LINK_RECOVERED,
    link_recovered_handler
)

adapter = CommunicationAdapter(
    event_bus
)

# Link goes down
adapter.process_report(
    "ISS",
    {
        "SNR (dB)": 15,
        "Status": "OFFLINE"
    }
)

# Link comes back
adapter.process_report(
    "ISS",
    {
        "SNR (dB)": 15,
        "Status": "ONLINE"
    }
)