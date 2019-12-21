#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('wolf/wolf-1.0b4.xml')
root = tree.getroot()

def get_lexical_entry(lemma):
    """
    lemma is the lexical word
    research the lemma in the XML and output the element of the tree
    """
    for element in tree.findall('./SYNSET'):
        if lemma == element.find('./SYNONYM/LITERAL').text:
            return element
    for element in tree.findall('./SYNSET'):
        for elmt in element.findall('./SYNONYM/LITERAL'):
            if lemma == elmt.text:
                return element
    return None

def get_hyperonym(lexical_entry):
    """
    Lexical_entry is the adress in the tree
    Get the hyperonym of the element
    """
    if lexical_entry != None:
        if lexical_entry.find('./ILR[@type="hypernym"]') != None:
            return lexical_entry.find('./ILR[@type="hypernym"]').text
        else:
            return lexical_entry.find('./ILR[@type="instance_hypernym"]').text
    return None

def find_primitive(ID):
    """
    ID = hyperonym of the tree
    Find the element with that ID in the tree
    """
    for element in tree.findall('./SYNSET'):
        if ID == element.find('./ID').text:
            return element
    raise ValueError('Word not found')

def get_from_P(ID_adress):
    '''
    ID_adress is the element in the tree corresponding to the primitive
    '''
    if ID_adress != None:
        return ID_adress.find('./ILR[@type="hypernym"]').text
    return None

#The fonction below is now useless for the loop because of the _ENTRY_ in LITERAL we can't go from Lemma to ID every times
def from_primitive_to_lemma(Primitive):
    """Primitive = element with the ID of the primitive
    get the lemma"""
    if Primitive != None:
        return Primitive.find('./SYNONYM/LITERAL').text
    return None
    #Btw, attention au différent LITERAL si il apparait en deuxième ou troisième position, il n'est pas pris en compte


def is_human(word):
    """
    word is currently the ID of a word (yeah we should change the name of that variable)
    so we can start the loop between ID to hypernym
    """
    current_loc = find_primitive(word)

    identifiant = current_loc.find('./ID').text
    #print('Emplacements',identifiant)
    if identifiant in ('eng-30-00007846-n','eng-30-00007846-n'):
        return True

    elif identifiant not in ('eng-30-00001740-n','eng-30-00002137-n'):
        identifiant = get_hyperonym(current_loc)
        return is_human(identifiant)

    return False

def is_human_from_noun(noun):
    return is_human(get_hyperonym(get_lexical_entry(noun)))
