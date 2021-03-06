import pygame


class Event:
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager"""

    def __init__(self, pygame_event: pygame.event.Event = None):
        self.pygame_event = pygame_event
        self.name = "Generic Event"


class TickEvent(Event):
    def __init__(self, pygame_event: pygame.event.Event):
        super().__init__(pygame_event)
        self.name = "Tick Event"


class QuitEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Quit Event"


class EventManager:
    """this object is responsible for coordinating most communication
    between the Model, View, and Controller."""

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners: WeakKeyDictionary = WeakKeyDictionary()

    def register_listener(self, listener):
        self.listeners[listener] = 1

    def unregister_listener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event: Event):
        for listener in self.listeners.keys():
            # NOTE: If the weakref has died, it will be
            # automatically removed, so we don't have
            # to worry about it.
            listener.notify(event)
