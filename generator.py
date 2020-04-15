import random as rd

class Generator:
    def __init__(self):
        pass

    def get_n_beats(self,n):
        beats = []
        for _ in range(n):
            beats.append(self.get_beat())

        return beats

    # note = [
    #   {0: tap, 1: accent}
    #   {0: single note, 1: flam, 2: diddle}
    #   {0: right, 1: left}
    # ]
    def get_beat(self):
        notes = []
        for _ in range(rd.randint(3,5)):
            notes.append([0,0,0])

        for note in notes:
            accent_toggle = rd.random()
            if accent_toggle < 0.5: note[0] = 1

            note_type = rd.random()
            if note_type >= 0.333 and note_type < 0.666: note[1] = 1
            elif note_type >= 0.666: note[1] = 2

            left_stick_toggle = rd.random()
            if left_stick_toggle < 0.5: note[2] = 1

        return notes
