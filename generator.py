import random as rd
from note_enum import NoteEnum
from note import Note

class Generator:
    def __init__(self):
        self.weights = {
            "articulation": [(NoteEnum.TAP, 0.75), (NoteEnum.ACCENT, 0.25)],
            "special": [(NoteEnum.PLAIN, 0.45), (NoteEnum.FLAM, 0.25), (NoteEnum.DIDDLE, 0.15), (NoteEnum.CHEESE, 0.15)],
            "sticking": [(NoteEnum.RIGHT, 0.5), (NoteEnum.LEFT, 0.5)]
        }

    def get_n_beats(self,n):
        beats = []
        for i in range(n):
            prev_beat_last_note = beats[i-1][-1] if i > 0 else None
            beats.append(self.get_beat(prev_beat_last_note))

        return beats


    def get_beat(self, prev_beat_last_note):
        notes = []
        for _ in range(rd.randint(3,5)):
            notes.append(Note())

        for idx, note in enumerate(notes):
            prev_note = None
            if idx > 0: prev_note = notes[idx-1]
            else: prev_note = prev_beat_last_note

            note.articulation = self._get_articulation(prev_note)
            note.special = self._get_special(prev_note)
            note.sticking = self._get_sticking(prev_note)

        return notes

    def _get_articulation(self, prev_note):
        return self._get_probablistic_from_arr(self.weights["articulation"])

    def _get_special(self, prev_note):
        return self._get_probablistic_from_arr(self.weights["special"])

    def _get_sticking(self, prev_note):
        if prev_note and prev_note.special in (NoteEnum.DIDDLE, NoteEnum.CHEESE):
            return NoteEnum.LEFT if prev_note.sticking == NoteEnum.RIGHT else NoteEnum.RIGHT
            
        return self._get_probablistic_from_arr(self.weights["sticking"])

    def _get_probablistic_from_arr(self, arr):
        rand = rd.random()
        tot = 0
        for val, chance in arr:
            tot += chance
            if rand < tot: return val

        # in case of 0.999..., try again
        return self._get_probablistic_from_arr(arr)
