#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:31:05 2019

@author: Thi & Lu & Edu
"""

#======================Imports=================================================
import codecs
import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
from dottize import *
import nouns_inflector
import pdb

#======================Lemmatizer SETUP========================================
nlp = spacy.load('fr')
pos = POSTagger()
french_lemmatizer = LefffLemmatizer(after_melt=True, default=True)
nlp.add_pipe(pos, name='pos', after='parser')
nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')

#=======================Global variables=======================================
list_epicene = []
epicenable_pos = ['NOUN', 'PROPN', 'ADJ', 'VERB', 'DET', 'ADP']

#===================Core of the program========================================
def main():
    doc = nlp("""La raison ne procède pas plus des autorités officieuses que des autorités officielles.
Ni le publiciste, ni le journaliste, ni le tribun, ni l'orateur, ni le conférencier ne sont aujourd'hui de
simples citoyens.
Le journaliste qui a trente ou cinquante ou quatre-vingts milliers de lecteurs, le conférencier qui
a régulièrement douze ou quinze cents spectateurs exercent en effet, comme le ministre,
comme le député, une autorité gouvernementale.""")
    #doc = nlp("""Les étudiants présentent leurs projets. Ils sont brillants !""")
    doc = preprocessing(doc)
    dottized_string = ''
    for word in doc:
        dottized_string += str(word.epicenize())+' '
    print(dottized_string)
    return dottized_string


def preprocessing(text):
    words_list= []
    for i in range(len(text)):
        words_list.append(Word(text[i].text,text[i].tag_,text[i].lemma_,i))
    return words_list

def sort(pre_processed_doc):
    epicenizable = list(filter(is_epicene,pre_processed_doc))
    print(epicenizable)
    return epicenizable
        

class Word():
    def __init__(self,form,pos,lemma,index):
        self.form = form
        self.pos = pos
        self.lemma = lemma
        self.index = index
        
    def pluralize(self):
        return pluralizer.pluralize(self.form)
    
    def dottize(self):
        if 'Plur' in self.pos:
            return dottize_plural(self.lemma)
        return dottize_singular(self.lemma)
    
    def is_epicene(self):
        if 'Noun' in self.pos:
            return nouns_inflector.get_grammatical_gender(self.lemma) == 'invariant'  #check LEMMA is epicene
    
    def epicenize(self):
        '''
        returns the dottized form is possible, 
        returns the word itself otherwise
        '''
        #Si le mot ne fait pas partie de la liste épicène
        if not self.is_epicene():
            if  'NOUN' in self.pos:
                pdb.set_trace()
                return self.dottize()
            elif 'PROPN' in self.pos:
                return self.form
            elif 'ADJ' in self.pos:
                return self.form
            elif 'VERB' in self.pos:
                return self.form  
            elif 'DET' in self.pos:
                return self.form  
            elif 'ADP' in self.pos:
                return self.form  
            else: #All the other POS
                return self.form
        #Si le mot est épicène : renvoie le mot original
        else:
            return self.form  
   

if __name__ == '__main__':
    main()