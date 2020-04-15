import inflect
inf = inflect.engine()

import json
import random as rd

from generator import Generator
from note_enum import NoteEnum

adjs = None
with open("adjectives.json") as json_file:
    adjs = json.load(json_file)

nouns = []
with open("nouns.txt", "r") as nouns_file:
    # print(nouns_file.readlines())
    for line in nouns_file.readlines():
        nouns.append(line[:-1])

def get_noun():
    noun = nouns[rd.randint(0, len(nouns)-1)]
    return noun[0].upper() + noun[1:]

def get_adjective():
    adj = adjs[rd.randint(0,len(adjs)-1)]
    return adj[0].upper() + adj[1:]

def get_title():
    plural = inf.plural(get_noun())
    rand = rd.random()
    # print(rand)
    # exit()

    if rand < 0.4:
        return plural
    elif rand < 0.65:
        return get_noun() + " " + plural
    elif rand < 0.85:
        return get_adjective() + " " + plural
    else:
        return get_adjective() + " " + get_noun() + " " + plural

notation_dict = dict()

for i in (NoteEnum.TAP, NoteEnum.ACCENT):
    for j in (NoteEnum.PLAIN, NoteEnum.FLAM, NoteEnum.DIDDLE, NoteEnum.CHEESE):
        for k in (NoteEnum.RIGHT, NoteEnum.LEFT):
            dict_key = str(i) + str(j) + str(k) #""+str(i)+str(j)+str(k)
            dict_val = "XX"
            # do stuff

            if j == NoteEnum.FLAM or j == NoteEnum.CHEESE: dict_val = "\\grace c''8" + " " + dict_val
            if j == NoteEnum.DIDDLE or j == NoteEnum.CHEESE: dict_val = dict_val + ":TT"



            if i == NoteEnum.ACCENT: dict_val = dict_val + "->"

            if k == NoteEnum.RIGHT: dict_val = dict_val + "-\"r\""
            else: dict_val = dict_val + "-\"l\""

            notation_dict[dict_key] = " " + dict_val + " "


g = Generator()
music_staff = ""

for beat in g.get_n_beats(1):
    num_notes = len(beat)
    is_odd_rhythm = num_notes % 2 == 1

    if is_odd_rhythm:
        music_staff += " \\tuplet "+ str(num_notes) + "/2 { "

    for idx, note in enumerate(beat):
        # print(note)
        key = str(note)
        # val notation_dict[key]
        note_split = notation_dict[key].split("XX")
        note_notation = "c''"
        tremolo_notation = "16"
        # if idx == 0:
        if is_odd_rhythm:
            note_notation += "8"
        else:
            note_notation += "16"
            tremolo_notation = "32"

        note_joined = note_notation.join(note_split)
        tremolo_split = note_joined.split("TT")
        final_note = tremolo_notation.join(tremolo_split)

        # print(final_note)
        music_staff += final_note

    if is_odd_rhythm:
        music_staff += " } "



staff = "{\n\\new PianoStaff << \n"
staff += "  \\new Staff {" + music_staff + "}\n"
staff += ">>\n}\n"

title = get_title().join("""\header {
  title = "TITLE"
  composer = "comp. a computer"
}""".split("TITLE"))

print(title + staff)
