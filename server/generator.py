import random as rd
from note_enum import NoteEnum
from note import Note


class Generator:
    def __init__(self, args):
        self.args = args
        # self.weights = {
        #     "articulation": [(NoteEnum.TAP, 0.75), (NoteEnum.ACCENT, 0.25)],
        #     "special": [(NoteEnum.PLAIN, 0.45), (NoteEnum.FLAM, 0.25), (NoteEnum.DIDDLE, 0.15), (NoteEnum.CHEESE, 0.15)],
        #     "sticking": [(NoteEnum.RIGHT, 0.5), (NoteEnum.LEFT, 0.5)]
        # }
        self.weights = dict()
        self.init_weights()
        self.sanitize_note_types()

    def sanitize_note_types(self):
        note_types = ()
        if not self.args.triplets and not self.args.sixteenths and not self.args.fivelets:
            self.args.triplets = True
            self.args.sixteenths = True
            self.args.fivelets = True

    def init_weights(self):
        # print(self.args)
        self.init_articulation()
        self.init_sticking()
        self.init_special()
        # exit()

    def init_special(self):
        self.weights["special"] = []
        spec_weights = dict()
        total_weight = 0
        for spec, enum_val in [("diddles", NoteEnum.DIDDLE), ("flams", NoteEnum.FLAM), ("cheeses", NoteEnum.CHEESE)]:
            weight = None
            try:
                weight = min(max(int(getattr(self.args, spec))/100, 0), 0.85)
            except:
                weight = 0.3
            finally:
                spec_weights[enum_val] = weight
                total_weight += weight

        if total_weight >= 0.85:
            spec_weights[NoteEnum.PLAIN] = 0.15
            total_weight += 0.15
        else:
            spec_weights[NoteEnum.PLAIN] = 1 - total_weight
            total_weight = 1

        for key in spec_weights.keys():
            spec_weights[key] /= total_weight
            self.weights["special"].append((key, spec_weights[key]))

    def init_articulation(self):
        freq = None
        try:
            freq = min(max(int(self.args.accents)/100, 0), 1)
        except:
            freq = 0.25
        finally:
            self.weights["articulation"] = [
                (NoteEnum.TAP, 1-freq),
                (NoteEnum.ACCENT, freq)
            ]

    def init_sticking(self):
        freq = None
        try:
            freq = min(max(int(self.args.rights)/100, 0.1), 0.9)
        except:
            freq = 0.5
        finally:
            self.weights["sticking"] = [
                (NoteEnum.LEFT, 1-freq),
                (NoteEnum.RIGHT, freq)
            ]

    def get_n_beats(self, n):
        beats = []
        for i in range(n):
            prev_beat_last_note = beats[i-1][-1] if i > 0 else None
            beats.append(self.get_beat(prev_beat_last_note))

        return beats

    def _generate_beat_notes(self):
        note_map = {
            3: "triplets",
            4: "sixteenths",
            5: "fivelets"
        }

        rand = None
        while not rand or not getattr(self.args, note_map[rand]):
            rand = rd.randint(3, 5)

        arr = []
        for _ in range(rand):
            arr.append(Note())

        return arr

    def get_beat(self, prev_beat_last_note):
        notes = self._generate_beat_notes()

        for idx, note in enumerate(notes):
            prev_note = None
            if idx > 0:
                prev_note = notes[idx-1]
            else:
                prev_note = prev_beat_last_note

            note.articulation = self._get_articulation(prev_note)
            note.special = self._get_special(prev_note)
            note.sticking = self._get_sticking(prev_note)

        return notes

    def _get_articulation(self, prev_note):
        return self._get_probablistic_from_arr(self.weights["articulation"])

    def _get_special(self, prev_note):
        val = self._get_probablistic_from_arr(self.weights["special"])

        # cannot play cheese/flam after cheese/diddle, try again
        if prev_note and prev_note.special in (NoteEnum.DIDDLE, NoteEnum.CHEESE) and val in (NoteEnum.FLAM, NoteEnum.CHEESE):
            return self._get_special(prev_note)

        return val

    def _get_sticking(self, prev_note):
        if prev_note and prev_note.special in (NoteEnum.DIDDLE, NoteEnum.CHEESE):
            return NoteEnum.LEFT if prev_note.sticking == NoteEnum.RIGHT else NoteEnum.RIGHT

        return self._get_probablistic_from_arr(self.weights["sticking"])

    def _get_probablistic_from_arr(self, arr):
        rand = rd.random()
        tot = 0
        for val, chance in arr:
            tot += chance
            if rand < tot:
                return val

        # in case of 0.999..., try again
        return self._get_probablistic_from_arr(arr)
