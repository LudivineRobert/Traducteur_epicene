#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:37:37 2019

@author: thibo
"""

import spacy
import get_relations
import primitives
import dottize
import det_rules
from os import listdir
#=====================PREPARATION==============================================

nlp = spacy.load('fr_core_news_sm')

def spot_nouns(doc):
    return list(filter(lambda word: word.pos_ == "NOUN", doc))

def epicenize(word, base_noun):
    """
    Takes a word object from the doc returns its dottized epicene form
    """
    
    try:
        if word.pos_ == 'ADJ':
            #pdb.set_trace()
            return dottize.dottize_adjective(word, base_noun)
        elif word.pos_ == 'NOUN':
            #pdb.set_trace()
            return dottize.dottize_noun(word, base_noun)
        elif word.pos_ == 'DET':
            return det_rules.epicenize_det(word.text)
        elif word.pos_ == 'VERB':
            return dottize.dottize_verb(word, base_noun)
        else:
            return word.text
    except(ValueError):
        return word.text

#=====================MAIN=====================================================

def process_file(filename):
    with open('inputs/'+filename, 'r') as input_file:
        content = input_file.read()
        doc = nlp(content)
    nouns_index = list(map(lambda word: word.i, spot_nouns(doc)))

    lists_index_to_epicenize = list()
    for i in nouns_index:
        #pdb.set_trace()
        try:
            if primitives.is_human_from_noun(doc[i].lemma_):
                lists_index_to_epicenize.append([i])
        except:
            None
    #pdb.set_trace()
    for j in lists_index_to_epicenize:
        j += get_relations.get_index_of_all_related_element(doc, j[0])
    print('\nIndexes of words to epicenize: {}'.format(lists_index_to_epicenize))
    
    output_list = [word.text for word in doc]
    
    for u in range(len(doc)):
        for l in lists_index_to_epicenize:
            if u in l:
                print('currently processed: {}'.format(doc[u].text))
                output_list[u] = epicenize(doc[u], base_noun = doc[l[0]])
                break
    
    output = ' '.join(output_list)
    new_file_path = 'outputs/epicene_'+filename
    with open(new_file_path, 'w+') as output_file:
        print(output, file = output_file)
        print("File created at {}".format(new_file_path))


def main():
    files = listdir('./inputs')
    for file in files:
        if 'epicene_'+file not in listdir('./outputs'):
            print('processing file "{}"'.format(file))
            process_file(file)
        else:
            print("file ""{}"" already processed".format(file))
    print('All the files have been processed')


if __name__ == '__main__':
    main()
