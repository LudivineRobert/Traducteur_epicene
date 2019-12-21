#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_index_of_determinants_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of determinant dependent to this noun
    """
    try:
        return [token.i for token in doc if token.dep_ ==
                "det" and token.head.pos_ ==
                "NOUN" and token.pos_ == "DET" and token.head.i ==
                noun_index][0]
    except BaseException:
        return None


def get_index_of_adpositions_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of preposition dependent to this noun
    """
    try:
        return [token.i for token in doc if token.dep_ == "case"
                and token.head.pos_ ==
                "NOUN" and token.pos_ == "ADP" and token.head.i ==
                noun_index][0]
    except BaseException:
        return None


def get_index_of_etre1_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of the past participle
    (with être as auxiliary) related to this noun,
    when the POS of syntactic head is NOUN
    """
    try:
        return [token.head.i for token in doc if
                (token.dep_ == "nsubj" or token.dep_ == "cop")
                and token.pos_ == "VERB" and token.head.pos_ ==
                "NOUN" and token.i == noun_index][0]
    except BaseException:
        return None


def get_index_of_etre2_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of the past participle
    (with être as auxiliary) related to this noun,
    when the POS of syntactic head is ADJ
    """
    try:
        return [token.head.i for token in doc if
                (token.dep_ == "nsubj" or token.dep_ == "cop")
                and token.pos_ == "NOUN" and (
                    token.head.pos_ == "ADJ" or token.head.pos_ == "VERB")
                and token.i == noun_index][0]
    except BaseException:
        return None


def get_index_of_etre3_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of the past participle
    (with être as auxiliary) related to this noun,
    when the POS of syntactic head is VERB
    """
    try:
        return [token.head.i for token in doc if
                (token.dep_ == "nsubj:pass" or token.dep_ == "cop")
                and token.pos_ == "NOUN" and token.head.pos_ == "VERB"
                and token.i == noun_index][0]
    except BaseException:
        return None


def get_index_of_avoir_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of the past participle
    (with avoir as auxiliary) related to this noun
    """
    try:
        for token in doc:
            if token.dep_ == "acl:relcl":
                for child in token.children:
                    if child.lemma_ == "avoir":
                        if token.head.i == noun_index:
                            return token.i
    except BaseException:
        return None


def get_index_of_adjectives_to_epicenize(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns the index of adjective dependent to this noun
    """
    try:
        return [token.i for token in doc if
                (token.dep_ == "amod" or token.dep_ == "nmod")
                and token.pos_ == "ADJ" and token.head.pos_ ==
                "NOUN" and token.head.i == noun_index][0]
    except BaseException:
        return None


def get_index_of_all_related_element(doc, noun_index):
    """
    Takes a spacy doc object and the index of a noun in this doc,
    returns a list of the indexes of all the tokens dependent to this noun
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
        if index_list[i] is None:
            del index_list[i]
    return index_list
