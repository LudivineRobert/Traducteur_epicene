#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:37:47 2019

@author: thibo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding=utf8
"""
Created on Thu Oct 24 11:41:27 2019

@author: thibo
"""

import re
import pluralizer
import pdb
import nouns_inflector


def get_noun_forms(noun):
    ''' 
    Takes a string which is a noun or an adjective, 
    returns a list of 2 elements : the masculine and feminine version.
    '''
    lexical_entry = nouns_inflector.get_lexical_entry(noun)
    gender = nouns_inflector.get_grammatical_gender(lexical_entry)
    if gender == ('masculine'):
        opposite_gender = nouns_inflector.get_feminine_form(lexical_entry)
    elif gender == 'feminine':
        opposite_gender = nouns_inflector.get_masculine_form(lexical_entry)
    else:
        return noun
    if opposite_gender != None:
        return (noun, opposite_gender)


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

def dottize_singular(noun):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the singular
    '''
    try:
        return concatenate_with_dot(*compare_strings(*get_noun_forms(noun)))
    except:
        return None
        #pdb.set_trace()

def dottize_plural(noun):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the plural
    '''
    try:
        if is_same_suffix(noun):
            return concatenate_with_dot(*compare_strings(*get_noun_forms(noun)),get_plural_suffix(noun))
        else:
            forms = get_noun_forms(noun)
            masc_plur = pluralizer.pluralize(forms[0])
            fem_plur = pluralizer.pluralize(forms[1])
            return concatenate_with_dot(*compare_strings(masc_plur,fem_plur))
    except:
        return None


def get_plural_suffix(singular_word):
    '''
    Takes a noun or adjective, 
    return its plural suffix. 
    '''
    morphemes = compare_strings(singular_word, pluralizer.pluralize(singular_word))
    suffix = morphemes[2]
    return suffix

def is_same_suffix(word):
    '''
    takes a noun or adjective, 
    return True if the plural suffixes are the same 
    for both masculine and feminine form
    '''
    forms = get_noun_forms(word)
    return get_plural_suffix(forms[0])==get_plural_suffix(forms[1])

def get_plural_forms(word):
    '''
    Takes a noun or adjective
    return a 2 elements list containing 
    its masculine and feminine plural suffixes
    '''
    if is_same_suffix(word):
        return get_plural_suffix(word)
    forms = get_word_forms(word)
    return [get_plural_suffix(forms[0]),get_plural_suffix(forms[0])]

