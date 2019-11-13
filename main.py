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
    #doc = nlp("""Nous sommes des étudiants très sérieux.""")
    doc = nlp("""Les étudiants présentent leurs projets. Ils sont brillants !""")
    extract_epicene_words_from_file()
    doc = preprocessing(doc)
    dottized_string = ''
    #sort(doc)
    for word in doc:
        #print(word.form, word.lemma)
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
        

def extract_epicene_words_from_file():
    fichier = codecs.open('list_epicene.txt','r','utf-8')
    words = fichier.read()
    global list_epicene 
    list_epicene = words.split('\n')

    fichier.close()

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
        return self.lemma in list_epicene #check LEMMA is epicene
    
    def epicenize(self):
        '''
        Takes a tuple as input (word, pos, lemma)
        returns its dottized form is possible, 
        returns the word itself otherwise
        '''
        #Si le mot ne fait pas partie de la liste épicène
        if not self.is_epicene():
            if  'NOUN' in self.pos or 'PROPN' in self.pos or 'ADJ' in self.pos:
                return self.dottize()
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