import inflect
inf = inflect.engine()

import json
import random as rd
from generator import Generator

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
    return get_adjective() + " " + get_noun() + " " + inf.plural(get_noun())

notation_dict = dict()

for i in range(2):
    for j in range(3):
        for k in range(2):
            dict_key = ""+str(i)+str(j)+str(k)
            dict_val = "XX"
            # do stuff

            if j == 1: dict_val = "\\grace c''8" + " " + dict_val
            if j == 2: dict_val = dict_val + ":16"

            if i == 1: dict_val = dict_val + "->"

            if k == 0: dict_val = dict_val + "-\"r\""
            else: dict_val = dict_val + "-\"l\""

            notation_dict[dict_key] = " " + dict_val + " "
            

g = Generator()
music_staff = ""

for beat in g.get_n_beats(3):
    num_notes = len(beat)
    is_odd_rhythm = num_notes % 2 == 1

    if is_odd_rhythm:
        music_staff += " \\tuplet "+ str(num_notes) + "/2 { "

    for idx, note in enumerate(beat):
        # print(note)
        key = ''.join(list(map(str,note)))
        # val notation_dict[key]
        note_split = notation_dict[key].split("XX")
        note_notation = "c''"
        if idx == 0:
            if is_odd_rhythm: note_notation += "8"
            else: note_notation += "16"


        music_staff += note_notation.join(note_split)

    if is_odd_rhythm:
        music_staff += " } "

staff = "{\n\\new PianoStaff << \n"
staff += "  \\new Staff {" + music_staff + "}\n"
staff += ">>\n}\n"

title = get_title().join("""\header {
  title = "TITLE"
  composer = "A Computer"
}""".split("TITLE"))

print(title + staff)
