#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:05 2019

@author: eduardo
"""

def get_index_of_determinants_to_epicenize(doc, noun_index):
    """
    takes a spacy doc object and the index of a noun in this doc,
    returns a list of the indexes of the determinants dependant to this noun
    """
    try:
        return [token.i for token in doc if token.dep_ == "det" and token.head.pos_ == "NOUN" and token.pos_ == "DET" and token.head.i == noun_index][0]
    except:
        return None

def get_index_of_adpositions_to_epicenize(doc, noun_index):
    """
    takes a spacy doc object and the index of a noun in this doc,
    returns a list of the indexes of the adpositions dependant to this noun
    """
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
    """
    takes a spacy doc object and the index of a noun in this doc,
    returns a list of the indexes of the adjectives dependant to this noun
    """
    try:
        return [token.i for token in doc if (token.dep_ == "amod" or token.dep_ == "nmod") and token.pos_ == "ADJ" and token.head.pos_ == "NOUN" and token.head.i == noun_index][0]
    except:
        return None

def get_index_of_all_related_element(doc, noun_index):
    """
    takes a spacy doc object and the index of a noun in this doc,
    returns a list of the indexes of all the tokens dependant to this noun
    """
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
