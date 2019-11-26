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

#def preprocessing(text):
#    for i in range(len(text)):
#        if 'NOUN' in text[i].pos_:
#            Noun(text[i].text,text[i].pos_,text[i].lemma_,i)
#        elif 'PRON' in text[i].pos_:
#            Pron(text[i].text,text[i].pos_,text[i].lemma_,i)
#        elif 'ADJ' in text[i].pos_:
#            Adj(text[i].text,text[i].pos_,text[i].lemma_,i)
#        else:
#            Word(text[i].text,text[i].pos_,text[i].lemma_,i)

def spot_nouns(doc):
    return list(filter(lambda word: word.pos_ == "NOUN", doc))

#=====================MAIN=====================================================

def main():
    doc = nlp("""Les journalistes sont très sérieux. Mais les boulangers, en revanche.. Les baguettes qu'ils ont préparées hier n'étaient pas délicieuses.""")
    print(doc)
    nouns_index = list(map(lambda word: word.i, spot_nouns(doc)))

    list_index_to_epicenize = list()
    set_index_to_epicenize = set()
    for i in nouns_index:
        #pdb.set_trace()
        if Primitives.is_human_from_noun(doc[i].lemma_):
            list_index_to_epicenize.append(i)
    #pdb.set_trace()
    for j in list_index_to_epicenize:
        set_index_to_epicenize.update(get_relations.get_index_of_all_related_element(doc, j))
    set_index_to_epicenize.update(list_index_to_epicenize)
    print('\nIndexes of words to epicenize: {}'.format(set_index_to_epicenize))
#    output_list = list_words
#    for u in range(len(list_words)):
#        if u in index_to_epicenize:
#            pdb.set_trace()
#            if list_words[u].pos in ['ADJ', 'NOUN']:
#                output_list[u] = output_list[u].epicenize()
#    print([word.pos for word in output_list])



if __name__ == '__main__':
    main()
