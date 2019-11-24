#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:37:37 2019

@author: thibo
"""

import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import pdb

import get_relations
import Primitives

#=====================PREPARATION==============================================

nlp = spacy.load('fr')
pos = POSTagger()
french_lemmatizer = LefffLemmatizer(after_melt=True, default=True)
nlp.add_pipe(pos, name='pos', after='parser')
nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')
    
def preprocessing(text):
    for i in range(len(text)):
        if 'NOUN' in text[i].tag_:
            Noun(text[i].text,text[i].tag_,text[i].lemma_,i)
        elif 'PRON' in text[i].tag_:
            Pron(text[i].text,text[i].tag_,text[i].lemma_,i)
        elif 'ADJ' in text[i].tag_:
            Adj(text[i].text,text[i].tag_,text[i].lemma_,i)
        else:
            Word(text[i].text,text[i].tag_,text[i].lemma_,i)

#=====================OBJECTS & CLASSES========================================
global list_words
list_words = []

class Word():
    def __init__(self,form,pos,lemma,index):
        self.form = form
        self.pos = pos
        self.lemma = lemma
        self.index = index
        list_words.append(self)


global list_nouns
list_nouns = []

class Noun(Word):
    def __init__(self,form,pos,lemma,index):
        super().__init__(form, pos, lemma, index)
        list_nouns.append(self)
    
    def refers_to_human(self):
        return Primitives.is_human_from_noun(self.lemma)
    def epicenize(self):
        pass

class Adj(Word):
    def __init__(self,form,pos,lemma,index):
        super().__init__(form, pos, lemma, index)

    def epicenize(self):
        pass

global list_pron
list_pron = []

class Pron(Word):
    def __init__(self,form,pos,lemma,index):
        super().__init__(form, pos, lemma, index)
        list_pron.append(self)
        
    def get_related_noun(self):
        pass
    def epicenize(self):
        pass
#=====================MAIN=====================================================

def main():
    doc = nlp("""Les journalistes du coin sont très sérieux. Mais les boulangers, en revanche.. Les baguettes qu'ils ont préparées hier n'étaient pas délicieuses.""")
    preprocessing(doc)
    
    index_to_epicenize = set()
    
    nouns_to_epicenize = []
    
    for noun in list_nouns:
        if noun.refers_to_human():
            nouns_to_epicenize.append(noun)
    pdb.set_trace()
    for noun in nouns_to_epicenize:
        pass
        #if allow_opposite_gender_form 
            #related_to_epicenize = get_relations.get_index()
            #index_to_epicenize.update(related_to_epicenize)
        
    #For all the stuff to epicenize, 
        #epicenize according to the rules
        
    #replace the elements in a copy of the original doc 
    
    #return the new string
    


if __name__ == '__main__':
    main()