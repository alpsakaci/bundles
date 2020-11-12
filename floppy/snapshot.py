from .models import NoteMemento


class NoteOriginator:

    def __init__(self, note):
        self.note = note

    def save_state_to_memento(self):
        return NoteMemento(title=self.note.title, content=self.note.title)

    def get_state_from_memento(self, memento):
        return (memento.title, memento.content)
