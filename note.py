from note_enum import NoteEnum

class Note:
    def __init__(self):
        self.articulation = NoteEnum.TAP
        self.special = NoteEnum.PLAIN
        self.sticking = NoteEnum.RIGHT

    def __str__(self):
        return str(self.articulation) + str(self.special) + str(self.sticking)
