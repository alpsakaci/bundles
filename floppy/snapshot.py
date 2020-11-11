from .models import NoteMemento

class NoteOriginator():
    _state = None

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state_to_memento(self):
        return NoteMemento(self._state)

    def get_state_from_memento(self, memento):
        self._state = memento.get_state()

