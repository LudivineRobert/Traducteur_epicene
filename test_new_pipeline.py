#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:37:37 2019

@author: thibo
"""

import spacy
from spacy_lefff import LefffLemmatizer, POSTagger

import get_relations

nlp = spacy.load('fr')
pos = POSTagger()
french_lemmatizer = LefffLemmatizer(after_melt=True, default=True)
nlp.add_pipe(pos, name='pos', after='parser')
nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')
    
def preprocessing(text:list)->list:
    words_list = []
    for i in range(len(text)):
        words_list.append(Word(text[i].text,text[i].tag_,text[i].lemma_,i))
    return words_list

class Word():
    def __init__(self,form,pos,lemma,index):
        self.form = form
        self.pos = pos
        self.lemma = lemma
        self.index = index


def spot_nouns(doc):
    nouns_list = []
    for word in doc:
        if 'NOUN' in word.pos:
            nouns_list.append(word)
    return nouns_list

def refers_to_human(word):
    return True

def get_related(word):
    pass

def main():
    doc = nlp("""Les journalistes du coin sont très sérieux. Mais les boulangers, en revanche.. Les baguettes qu'ils ont préparées hier n'étaient pas délicieuses.""")
    doc = preprocessing(doc)
    
    index_to_epicenize = {}
    
    list_nouns = spot_nouns(doc)
    
    nouns_to_epicenize = []
    
    for noun in list_nouns:
        if refers_to_human(noun):
            nouns_to_epicenize.append(noun)
    
    for noun in nouns_to_epicenize:
        #related_to_epicenize = get_relations.get_index()
        index_to_epicenize.update(related_to_epicenize)
        
    #For all the stuff to epicenize, 
        #epicenize according to the rules
        
    #replace the elements in a copy of the original doc 
    
    #return the new string
    


if __name__ == '__main__':
    main()