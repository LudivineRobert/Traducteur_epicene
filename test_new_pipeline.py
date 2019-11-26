#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:37:37 2019

@author: thibo
"""
import pdb

import spacy
import dottize
import get_relations
import Primitives
import nouns_inflector
import adj_inflector

#=====================PREPARATION==============================================

nlp = spacy.load('fr_core_news_sm')

def preprocessing(text):
    for i in range(len(text)):
        if 'NOUN' in text[i].pos_:
            Noun(text[i].text,text[i].pos_,text[i].lemma_,i)
        elif 'PRON' in text[i].pos_:
            Pron(text[i].text,text[i].pos_,text[i].lemma_,i)
        elif 'ADJ' in text[i].pos_:
            Adj(text[i].text,text[i].pos_,text[i].lemma_,i)
        else:
            Word(text[i].text,text[i].pos_,text[i].lemma_,i)

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
        self.gender = nouns_inflector.get_gender(self.form)
        self.number = nouns_inflector.get_number(self.form)

    @property
    def refers_to_human(self):
        return Primitives.is_human_from_noun(self.lemma)

    def epicenize(self):
        try:
            if self.number == 'plural':
                return dottize.dottize_plural_noun(self.lemma)
            elif self.number == 'singular':
                return dottize.dottize_singular_noun(self.lemma)
        except:
            return self.form

class Adj(Word):
    def __init__(self,form,pos,lemma,index):
        super().__init__(form, pos, lemma, index)
        self.gender = adj_inflector.get_gender(self.form)
        self.number = adj_inflector.get_number(self.form)

    def epicenize(self):
        try:
            if self.number == 'plural':
                return dottize.dottize_plural_adj(self.lemma)
            elif self.number == 'singular':
                return dottize.dottize_singular_adj(self.lemma)
        except:
            return self.form

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
    doc = nlp("""Les journalistes sont très sérieux. Mais les boulangers, en revanche.. Les baguettes qu'ils ont préparées hier n'étaient pas délicieuses.""")
    preprocessing(doc)

    index_to_epicenize = set()

    nouns_to_epicenize = []
    for noun in list_nouns:
        if noun.refers_to_human:
            index_to_epicenize.append(noun)
            index_to_epicenize.add(noun.index)
    #pdb.set_trace()
    for noun in nouns_to_epicenize:
        index_to_epicenize.update(get_relations.get_index_of_all_related_element(doc, noun.index))
    print(index_to_epicenize)
    output_list = list_words
    for u in range(len(list_words)):
        if u in index_to_epicenize:
            pdb.set_trace()
            if list_words[u].pos in ['ADJ', 'NOUN']:
                output_list[u] = output_list[u].epicenize()
    print([word.pos for word in output_list])



if __name__ == '__main__':
    main()
