from EventBus import EventBus

class EndGameListener:

    def __init__(self, event_bus):
        self.event_bus = event_bus
