#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:05 2019

@author: edu
"""

import spacy

nlp = spacy.load('fr_core_news_sm') # some data are wrong

text = ("Ni le publiciste que j'ai rencontré hier, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de simples citoyens.")
#text = ("j'ai mangé le pomme")
#text = ("j'ai mangé le pomme. la pomme que j'ai mangée. la tortue que j'ai adoptée. la ville où je suis allé.")
#text = ("la ville où je suis allé. la pomme que j'ai mangée. Les grands bâtiments sont habités par des vieux.")
#text = ("j'ai mangé la pomme rouge de l'oratrice que j'ai rencontrée.")
#text = ("L'auteur que j'ai rencontré était intéressant.")
#text = ("le port où le publiciste est allée. la pomme que j'ai mangée. les beaux enfants jouent dans le parc.")
#text = ("la belle oratrice est très fatigué")

doc = nlp(text)

def spot_nouns():
    return list(filter(lambda word: word.pos_ == "NOUN", doc)) ### USE THIS FUNCTION TO SPOT ALL NOUNS IN DOC

def spot_nouns_index():
    return list(map(lambda word: word.i, spot_nouns())) ### USE THIS FUNCTION TO SPOT INDEX OF ALL NOUNS IN DOC

def nouns_indexes():
    return list(zip(spot_nouns(), spot_nouns_index())) ### RETURNS A LIST OF TUPLES WITH ALL NOUN-INDEX PAIRS IN DOC

#### FUNCTIONS ####

def get_index_of_determinants_to_epicenize(doc, noun_index):
    try:
        return [token.i for token in doc if token.dep_ == "det" and token.head.pos_ == "NOUN" and token.pos_ == "DET" and token.head.i == noun_index][0]
    except:
        return None

def get_index_of_adpositions_to_epicenize(doc, noun_index):
    try:
        return [token.i for token in doc if token.dep_ == "case" and token.head.pos_ == "NOUN" and token.pos_ == "ADP" and token.head.i == noun_index][0]
    except:
        return None

def get_index_of_etre1_to_epicenize(doc, noun_index): # when head is NOUN
    try:
        return [token.head.i for token in doc if (token.dep_ == "nsubj" or token.dep_ == "cop") and token.pos_ == "VERB" and token.head.pos_ == "NOUN" and token.i == noun_index][0]
    except: return None

def get_index_of_etre2_to_epicenize(doc, noun_index): # when head is ADJ
    try:
        return [token.head.i for token in doc if (token.dep_ == "nsubj" or token.dep_ == "cop") and token.pos_ == "NOUN" and (token.head.pos_ == "ADJ" or token.head.pos_ == "VERB") and token.i == noun_index][0]
    except:
        return None

def get_index_of_etre3_to_epicenize(doc, noun_index): # when head is VERB
    try:
        return [token.head.i for token in doc if (token.dep_ == "nsubj:pass" or token.dep_ == "cop") and token.pos_ == "NOUN" and token.head.pos_ == "VERB" and token.i == noun_index][0]
    except:
        return None

def get_index_of_avoir_to_epicenize(doc, noun_index):
    try:
        for token in doc:
            if token.dep_ == "acl:relcl":
                for child in token.children:
                    if child.lemma_ == "avoir":
                        if token.head.i == noun_index:
                            return token.i
    except:
        return None


def get_index_of_adjectives_to_epicenize(doc, noun_index):
    try:
        return [token.i for token in doc if (token.dep_ == "amod" or token.dep_ == "nmod") and token.pos_ == "ADJ" and token.head.pos_ == "NOUN" and token.head.i == noun_index][0]
    except:
        return None


def get_index_of_all_related_element(doc, noun_index):
    index_list = []
    index_list.append(get_index_of_determinants_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_adpositions_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_etre1_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_etre2_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_etre3_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_avoir_to_epicenize(doc, noun_index))
    index_list.append(get_index_of_adjectives_to_epicenize(doc, noun_index))
    for i in reversed(range(len(index_list))):
        if index_list[i] == None:
            del index_list[i]
    return index_list

#print(get_index_of_all_related_element(doc,29))

#print(get_index_of_determinants_to_epicenize(doc,8))
#print(get_index_of_adpositions_to_epicenize(doc,8))
#print(get_index_of_etre1_to_epicenize(doc,8))
#print(get_index_of_etre2_to_epicenize(doc,8))
#print(get_index_of_etre3_to_epicenize(doc,8))
#print(get_index_of_avoir_to_epicenize(doc,8))
#print(get_index_of_adjectives_to_epicenize(doc,8))

#### SMALL PIPELINE MODIFICATION: I COULDN'T TAKE ONLY A WORD AS INPUT.
#### DOING THAT WAY YOU LOSE ALL THE RELATIONS. SO I TOOK THE WHOLE DOC AS INPUT.
#### OUTPUTS OF THESE FUNCTIONS ARE LIST OF TUPLES CONTAINING 2 ELEMENTS:
#### 1) INDEX OF WORD EVENTUALLY TO BE MODIFIED 2) INDEX OF THE NOUN LINKED TO EACH WORD.
#### NOUNS ARE ALREADY EXTRACTED WITH SPOT_NOUNS IN THIS FILE

#### I THINK WE DON'T NEED LEFFF ANYMORE

#### NOTE: WHEN RELATION IS "ROOT" THERE'S NO WAY TO KEEP THE RELATIONS WE NEED.
#### HOPEFULLY THE CASES AREN'T SO NUMEROUS
