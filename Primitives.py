# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:26:32 2019

@author: rog
"""

import xml.etree.ElementTree as ET

tree = ET.parse('wolf/wolf-1.0b4.xml')
root = tree.getroot()

#First : find the word in the xml " >WORD</LITERAL> "
# Second : Find the hypernym and go to the hyperonyms
#Third : go to the upper Hypernym : physical existence or not, and HUMAN


def get_lexical_entry(lemma):
    """
    lemma is the lexical word
    research the lemma in the XML and output the element of the tree
    """
    for element in tree.findall('./SYNSET'):
        if lemma == element.find('./SYNONYM/LITERAL').text:
            return element
    return None

test = get_lexical_entry('bouteille')
print('lexic_entry', test)

def get_hyperonym(lexical_entry):
    """
    Lexical_entry is the adress in the tree
    Get the hyperonym of the element
    """
    if lexical_entry != None:   
        return lexical_entry.find('./ILR[@type="hypernym"]').text
    return None

test_h = get_hyperonym(test)

print('hyperonyme: ', test_h)

def find_primitive(ID):
    """
    ID = hyperonym of the tree 
    Find the element with that ID in the tree
    """
    for element in tree.findall('./SYNSET'):
        if ID == element.find('./ID').text:
            return element
        
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
    

def looking_for_human(word):
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
        return looking_for_human(identifiant)

    return False

#===============================Test============================================

from_primitive_to_lemma(find_primitive(test_h))
Noun_list = ['étudiant', 'boulanger','bouteille','verre','chèvre','souris']

for Noun in Noun_list :
    print('Voici le nom traité :', Noun)
    if looking_for_human(get_hyperonym(get_lexical_entry(Noun))):
        print("It's a human being")
    else: 
        print("it's not human")

#ON peut aller depuis l'ID du mot mais qu'en est-il du mot ?
    