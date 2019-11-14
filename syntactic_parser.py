#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:05 2019

@author: edu
"""

import spacy

nlp = spacy.load('fr_core_news_sm')

#text = ("Ni le publiciste que j'ai rencontré hier, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de simples citoyens.")
#text = ("j'ai mangé le pomme")
#text = ("j'ai mangé le pomme. la pomme que j'ai mangée. la tortue que j'ai adoptée. la ville où je suis allé.")
text = ("la ville où je suis allé. la pomme que j'ai mangée. les beaux enfants jouent dans le parc.")
#text = ("j'ai mangé la pomme rouge.")
doc = nlp(text)

# whole syntax tree
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])

# what we need
def get_adj(): # NO appos:nmod
    '''Takes doc as input and returns a list of 2-tuples with ADJ, and related noun'''
    return [(token.text, token.head.text) for token in doc if token.dep_ == "amod" or token.dep_ == "nmod"]

def get_relative_clauses():
    '''Takes doc as input and returns a list of 3-tuples
    containing a word-form (VERB), related noun (acl:relcl)
    and a list containing inflected avoir or empty list if AUX = etre'''
    return [(token.text,
             token.head.text,
             [child for child in token.children if child.lemma_ == "avoir"]) for token in doc if token.dep_ == "acl:relcl"]

#def get_aux(text): # I consider copulas and auxiliaries be part of same category
#    '''Takes a text as input and returns a list of 4-tuples with word-form, lemma, relation and related noun, only if word-form is AUX'''
#    return [(token.text, token.lemma_, token.head.text, [str(child) for child in token.children]) for token in doc if token.dep_ == "aux" or token.dep_ == "cop"]

adj = get_adj()
rel_clause = get_relative_clauses()

print(rel_clause)
print(adj)

for relation in rel_clause: # prints the name related to "avoir" that must be handled somehow
    if relation[2] != []:
        print(relation[1])