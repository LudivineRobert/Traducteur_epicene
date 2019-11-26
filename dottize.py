#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:37:47 2019

@author: thibo
"""

import re
import pdb
import adj_inflector
import nouns_inflector

#=========================-----================================================
#=========================Nouns================================================
#=========================-----================================================


def get_noun_forms(noun):
    ''' 
    Takes a string which is a noun or an adjective, 
    returns a list of 2 elements : the masculine and feminine version.
    '''
    gender = nouns_inflector.get_gender(noun)
    if gender == ('masculine'):
        masculine = noun
        feminine = nouns_inflector.get_feminine(noun)
    elif gender == 'feminine':
        feminine = noun
        masculine = nouns_inflector.get_masculine(noun)
    else:
        return noun
    return (masculine, feminine)




def dottize_singular_noun(noun):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the singular
    '''
    try:
        if type(get_noun_forms(noun)) == str:
            return concatenate_with_dot(*compare_strings(get_noun_forms(noun)))
        else:
            return concatenate_with_dot(*compare_strings(*get_noun_forms(noun)))
    except:
        return None
        #pdb.set_trace()

def dottize_plural_noun(noun):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the plural
    '''
    try:
        if is_same_suffix_noun(noun):
            if type(get_noun_forms(noun)) == str:
                return concatenate_with_dot(*compare_strings(get_noun_forms(noun)),get_plural_suffix_noun(noun))
            else:
                return concatenate_with_dot(*compare_strings(*get_noun_forms(noun)),get_plural_suffix_noun(noun))
                
        else:
            forms = get_noun_forms(noun)
            masc_plur = nouns_inflector.pluralize(forms[0])
            fem_plur = nouns_inflector.pluralize(forms[1])
            return concatenate_with_dot(*compare_strings(masc_plur,fem_plur))
    except:
        return None


def get_plural_suffix_noun(singular_word):
    '''
    Takes a noun or adjective, 
    return its plural suffix. 
    '''
    number = nouns_inflector.get_number(singular_word)
    if number == 'plur':
        singular_word = nouns_inflector.singularize(singular_word)
    morphemes = compare_strings(singular_word, nouns_inflector.pluralize(singular_word))
    suffix = morphemes[2]
    return suffix

def is_same_suffix_noun(word):
    '''
    takes a noun or adjective, 
    return True if the plural suffixes are the same 
    for both masculine and feminine form
    '''
    forms = get_noun_forms(word)
    return get_plural_suffix_noun(forms[0])==get_plural_suffix_noun(forms[1])

def get_plural_forms_noun(word):
    '''
    Takes a noun or adjective
    return a 2 elements list containing 
    its masculine and feminine plural suffixes
    '''
    if is_same_suffix_noun(word):
        return get_plural_suffix_noun(word)
    forms = get_noun_forms(word)
    return [get_plural_suffix_noun(forms[0]),get_plural_suffix_noun(forms[0])]



#=========================----------===========================================
#=========================Adjectives===========================================
#=========================----------===========================================

def get_adj_forms(adj):
    ''' 
    Takes a string which is an adjective, 
    returns a list of 2 elements : the masculine and feminine version.
    '''
    gender = adj_inflector.get_gender(adj)
    if gender == ('masculine'):
        masculine = adj
        feminine = adj_inflector.get_feminine(adj)
    elif gender == 'feminine':
        feminine = adj
        masculine = adj_inflector.get_masculine(adj)
    else:
        return adj
    return (masculine, feminine)


def get_plural_forms_adj(word):
    '''
    Takes an adjective
    return a 2 elements list containing 
    its masculine and feminine plural suffixes
    '''
    if is_same_suffix_adj(word):
        return get_plural_suffix_adj(word)
    forms = get_adj_forms(word)
    return [get_plural_suffix_adj(forms[0]),get_plural_suffix_adj(forms[0])]


def get_plural_suffix_adj(singular_word):
    '''
    Takes a noun or adjective, 
    return its plural suffix. 
    '''
    number = adj_inflector.get_number(singular_word)
    if number == 'plur':
        singular_word = adj_inflector.singularize(singular_word)
    morphemes = compare_strings(singular_word, adj_inflector.pluralize(singular_word))
    suffix = morphemes[2]
    return suffix


def is_same_suffix_adj(word):
    '''
    takes an adjective, 
    return True if the plural suffixes are the same 
    for both masculine and feminine form
    '''
    forms = get_adj_forms(word)
    return get_plural_suffix_adj(forms[0])==get_plural_suffix_adj(forms[1])



def dottize_plural_adj(adj):
    '''
    Takes an adjective
    Turns it into its dottized form, in the plural
    '''
    try:
        #pdb.set_trace()
        if is_same_suffix_adj(adj):
            if type(get_adj_forms(adj)) == str:
                return concatenate_with_dot(*compare_strings(get_adj_forms(adj)),get_plural_suffix_adj(adj))
            else:
                return concatenate_with_dot(*compare_strings(*get_adj_forms(adj)),get_plural_suffix_adj(adj))
                
        else:
            forms = get_adj_forms(adj)
            masc_plur = adj_inflector.pluralize(forms[0])
            fem_plur = adj_inflector.pluralize(forms[1])
            return concatenate_with_dot(*compare_strings(masc_plur,fem_plur))
    except:
        return None

def dottize_singular_adj(adj):
    '''
    Takes an adjective
    Turns it into its dottized form, in the singular
    '''
    try:
        if type(get_adj_forms(adj)) == str:
            return concatenate_with_dot(*compare_strings(get_adj_forms(adj)))
        else:
            return concatenate_with_dot(*compare_strings(*get_adj_forms(adj)))
    except:
        return None


#=========================-------==============================================
#=========================Generic==============================================
#=========================-------==============================================

def compare_strings(masc,fem = ''):
    '''
    Input : 2 strings
    output : a tuple of 3 elements, which are :
    the common part, the rest of the 1st string, the rest of the 2d string
    '''
    common = str()
    masc_rest = str()
    fem_rest = str()
    
    min_len = min(len(masc), len(fem))
    
    i=0
    while i < min_len and masc[i] == fem[i]:
        common += masc[i]
        i += 1
    masc_rest = masc[i:]
    fem_rest = fem[i:]
    return(common, masc_rest, fem_rest) #tuple
    
    
def concatenate_with_dot(*strings):
    '''
    input : an unknown number of strings
    concatenate those strings with the middle dot 
    '''
    useful_elements = []
    for i in strings:
        if i != '':
            useful_elements.append(i)
    return "·".join(useful_elements)

