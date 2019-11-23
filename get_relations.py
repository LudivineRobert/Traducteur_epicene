#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:05 2019

@author: edu
"""

import spacy

nlp = spacy.load('fr_core_news_sm') # some data are wrong

#text = ("Ni le publiciste que j'ai rencontré hier, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de simples citoyens.")
#text = ("j'ai mangé le pomme")
#text = ("j'ai mangé le pomme. la pomme que j'ai mangée. la tortue que j'ai adoptée. la ville où je suis allé.")
#text = ("la ville où je suis allé. la pomme que j'ai mangée. Les grands bâtiments sont habités par des vieux.")
text = ("j'ai mangé la pomme rouge de l'oratrice que j'ai rencontré.")
#text = ("L'auteur que j'ai rencontré était intéressant.")
#text = ("le port où le publiciste est allée. la pomme que j'ai mangée. les beaux enfants jouent dans le parc.")
#text = ("la belle oratrice est très fatigué")

doc = nlp(text)

# whole syntax tree #### for test ####
for token in doc:
    print(token.text, token.pos_, token.i, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
######################################

#### FUNCTIONS ####

def get_index_of_determinants_to_epicenize(doc):
    return [(token.i, token.head.i) for token in doc if token.dep_ == "det" and token.head.pos_ == "NOUN" and token.pos_ == "DET"]


def get_index_of_adpositions_to_epicenize(doc):
    return [(token.i, token.head.i) for token in doc if token.dep_ == "case" and token.head.pos_ == "NOUN" and token.pos_ == "ADP"]


def get_index_of_etre1_to_epicenize(doc): # when head is NOUN
    return [(token.head.i, token.i) for token in doc if (token.dep_ == "nsubj" or token.dep_ == "cop") and token.pos_ == "VERB" and token.head.pos_ == "NOUN"]

def get_index_of_etre2_to_epicenize(doc): # when head is ADJ
    return [(token.head.i, token.i) for token in doc if (token.dep_ == "nsubj" or token.dep_ == "cop") and token.pos_ == "NOUN" and (token.head.pos_ == "ADJ" or token.head.pos_ == "VERB")]

def get_index_of_etre3_to_epicenize(doc): # when head is VERB
    return [(token.head.i, token.i) for token in doc if (token.dep_ == "nsubj:pass" or token.dep_ == "cop") and token.pos_ == "NOUN" and token.head.pos_ == "VERB"]


def get_index_of_avoir_to_epicenize(doc):
    for token in doc:
        if token.dep_ == "acl:relcl":
            for child in token.children:
                if child.lemma_ == "avoir":
                    return [(token.i, token.head.i)]


def get_index_of_adjectives_to_epicenize(doc):
    return [(token.i, token.head.i) for token in doc if (token.dep_ == "amod" or token.dep_ == "nmod") and token.pos_ == "ADJ" and token.head.pos_ == "NOUN"]



print(get_index_of_determinants_to_epicenize(doc))
print(get_index_of_adpositions_to_epicenize(doc))
print(get_index_of_etre1_to_epicenize(doc))
print(get_index_of_etre2_to_epicenize(doc))
print(get_index_of_etre3_to_epicenize(doc))
print(get_index_of_avoir_to_epicenize(doc))
print(get_index_of_adjectives_to_epicenize(doc))

#### SMALL PIPELINE MODIFICATION: I COULDN'T TAKE ONLY A WORD AS INPUT.
#### IN THAT WAY I LOST ALL THE RELATIONS. SO I TOOK THE WHOLE DOC AS INPUT.
#### OUTPUTS OF THESE FUNCTIONS ARE LIST OF TUPLES CONTAINING 2 ELEMENTS:
#### 1) INDEX OF WORD EVENTUALLY TO BE MODIFIED 2) INDEX OF THE NOUN LINKED TO EACH WORD.
#### YOU CAN EXTRACT THE LIST OF NOUNS (WHICH ONLY NOW PASS THROUGH THE REFERS_TO_HUMAN FUNCTION)
#### BY TAKING FOR EACH TUPLE INDEX[1]
#### I THINK WE DON'T NEED LEFFF ANYMORE

#### NOTE: WHEN RELATION IS "ROOT" THERE'S NO WAY TO KEEP THE RELATIONS WE NEED.
#### HOPEFULLY THE CASES AREN'T SO NUMEROUS