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

from bs4 import BeautifulSoup as bs
import requests
import re
import pluralizer
import pdb


def get_word_forms(string):
    ''' 
    Takes a string which is a noun or an adjective NON EPICENE, 
    returns a list of 2 elements : the masculine and feminine version.
    '''
    url = 'https://larousse.fr/dictionnaires/francais/'+string+'/'
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    #Using the Larousse website
    soup = bs(response.content,'html.parser')
    try:
        forms = soup.find(class_='AdresseDefinition').text
    except:
        return None
        #pdb.set_trace()
    forms = forms[1::]
    forms = forms.split(', ')
    #If the list contains 2 elements 
    if len(forms) > 1:
        return forms
    #Else (as sometimes the dictionairy messes up)
    #we need to extract the next word in the list of word
    #of the dictionnary
    else:
        #Taking the complete url we have been redirected to 
        complete_url = response.url
        #using regex to extract the id number of the word 
        number = re.split('(?<=\/)(\d+)',complete_url)
        number = number[1]
        number = int(number)
        #increasing of 1  this id number
        number = number + 1
        #including this number in the url from above 
        url2 = url+str(number)
        #Do another request 
        response2 =  requests.get(url2,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        soup2 = bs(response2.content,'html.parser')
        forms2 = soup2.find(class_='AdresseDefinition').text
        forms2 = forms2[1::]
        #merge the two lists of 1 element to get a list of 2 elements
        forms.append(forms2)
        return forms
     
def compare_strings(masc,fem):
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

def dottize_singular(word):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the singular
    '''
    try:
        return concatenate_with_dot(*compare_strings(*get_word_forms(word)))
    except:
        return None
        #pdb.set_trace()

def dottize_plural(word):
    '''
    Takes a noun or adjective
    Turns it into its dottized form, in the plural
    '''
    try:
        if is_same_suffix(word):
            return concatenate_with_dot(*compare_strings(*get_word_forms(word)),get_plural_suffix(word))
        else:
            forms = get_word_forms(word)
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
    forms = get_word_forms(word)
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

