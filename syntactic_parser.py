#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:05 2019

@author: edu
"""

import spacy

nlp = spacy.load('fr_core_news_sm')

#text = ("Ni le publiciste, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de simples citoyens.")
#text = ("j'ai mangé le pomme")
text = ("Ni le publiciste, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de simples citoyens. Un journaliste qui joue avec les ministères et qui argue du simple citoyen n'est pas recevable.")
doc = nlp(text)

# whole syntax tree
#for token in doc:
#    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])

# what we need
def get_adj(text):
    '''Takes a text as input and returns a list of 3-tuples with word-form, pos and related noun, only if word-form is ADJ'''
    return [(token.text, token.dep_, token.head.text) for token in doc if token.dep_ == "amod"]

def get_aux(text): # I consider copulas and auxiliaries be part of same category
    '''Takes a text as input and returns a list of 3-tuples with word-form, pos and related noun, only if word-form is AUX'''
    return [(token.text, token.dep_, token.head.text) for token in doc if token.dep_ == "aux" or token.dep_ == "cop"]

adj = print(get_adj(text))
aux = print(get_aux(text))