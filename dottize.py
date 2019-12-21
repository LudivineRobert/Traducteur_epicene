#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import adj_inflector
import nouns_inflector


def dottize_verb(word, base_noun):
    """
    Takes a verb spacy word object and its head noun,
    returns its dottized epicene form
    """
    if nouns_inflector.get_number(base_noun.text) == 'singular':
        return concatenate_with_dot(word.text, 'e')
    else:
        return concatenate_with_dot(word.text, 'e', 's')


def dottize_adjective(word, base_noun):
    """
    Takes an adjective spacy word object and its head noun,
    returns its dottized epicene form
    """
    if adj_inflector.get_gender(word.text) == 'invariant':
        return word.text
    forms = get_adj_forms(word.text)
    comp = compare_strings(*forms)
    if nouns_inflector.get_number(base_noun.text) == 'plural':
        if is_same_suffix_adj(word, forms):
            suffix = get_plural_suffix_adj(forms[0])
            return concatenate_with_dot(comp[0], comp[1], comp[2], suffix)
        else:
            suffix1 = get_plural_suffix_adj(forms[0])
            suffix2 = get_plural_suffix_adj(forms[0])
            return concatenate_with_dot(
                comp[0], comp[1] + suffix1, comp[2] + suffix2)
    else:
        return concatenate_with_dot(comp[0], comp[1], comp[2])


def dottize_noun(word, base_noun):
    """
    Takes a noun spacy word object and its head noun (itself),
    returns its dottized epicene form
    """
    if nouns_inflector.get_gender(word.text) == 'invariant':
        return word.text
    forms = get_noun_forms(word.text)
    comp = compare_strings(*forms)

    if nouns_inflector.get_number(base_noun.text) == 'plural':

        if is_same_suffix_noun(word, forms):
            suffix = get_plural_suffix_noun(forms[0])
            return concatenate_with_dot(comp[0], comp[1], comp[2], suffix)
        else:
            suffix1 = get_plural_suffix_noun(forms[0])
            suffix2 = get_plural_suffix_noun(forms[0])
            return concatenate_with_dot(
                comp[0], comp[1] + suffix1, comp[2] + suffix2)
    else:
        return concatenate_with_dot(comp[0], comp[1], comp[2])


def get_plural_suffix_adj(singular_word):
    """
    Takes a noun or adjective,
    return its plural suffix.
    """
    morphemes = compare_strings(singular_word,
                                adj_inflector.pluralize(singular_word))
    suffix = morphemes[2]
    return suffix


def get_plural_suffix_noun(singular_word):
    """
    Takes a noun or adjective,
    return its plural suffix.
    """
    morphemes = compare_strings(singular_word,
                                nouns_inflector.pluralize(singular_word))
    suffix = morphemes[2]
    return suffix


def is_same_suffix_adj(word, forms):
    """
    Takes an adjective,
    return True if the plural suffixes are the same
    for both masculine and feminine form
    """
    return get_plural_suffix_adj(forms[0]) == get_plural_suffix_adj(forms[1])


def is_same_suffix_noun(word, forms):
    """
    Takes an adjective,
    return True if the plural suffixes are the same
    for both masculine and feminine form
    """
    return get_plural_suffix_noun(forms[0]) == get_plural_suffix_noun(forms[1])


def get_adj_forms(adj):
    """
    Takes a string which is an adjective,
    returns a list of 2 elements : the masculine and feminine version.
    """
    gender = adj_inflector.get_gender(adj)
    number = adj_inflector.get_number(adj)
    if number == 'plural':
        adj = adj_inflector.singularize(adj)
    if gender == ('masculine'):
        masculine = adj
        feminine = adj_inflector.get_feminine(adj)
    elif gender == 'feminine':
        feminine = adj
        masculine = adj_inflector.get_masculine(adj)
    else:
        masculine = adj
        feminine = masculine
    return (masculine, feminine)


def get_noun_forms(noun):
    """
    Takes a string which is an adjective,
    returns a list of 2 elements : the masculine and feminine version.
    """
    gender = nouns_inflector.get_gender(noun)
    number = nouns_inflector.get_number(noun)
    if number == 'plural':
        noun = nouns_inflector.singularize(noun)
    if gender == ('masculine'):
        masculine = noun
        feminine = nouns_inflector.get_feminine(noun)
    elif gender == 'feminine':
        feminine = noun
        masculine = nouns_inflector.get_masculine(noun)
    else:
        feminine = noun
        masculine = noun
    return (masculine, feminine)


def compare_strings(masc, fem=''):
    """
    Input : 2 strings
    output : a tuple of 3 elements, which are :
    the common part, the rest of the 1st string, the rest of the 2d string
    """
    common = str()
    masc_rest = str()
    fem_rest = str()

    min_len = min(len(masc), len(fem))

    i = 0
    while i < min_len and masc[i] == fem[i]:
        common += masc[i]
        i += 1
    masc_rest = masc[i:]
    fem_rest = fem[i:]
    return(common, masc_rest, fem_rest)  # tuple


def concatenate_with_dot(*strings):
    """
    Takes an unknown number of strings
    concatenate those strings with the middle dot
    """
    useful_elements = []
    for i in strings:
        if i != '':
            useful_elements.append(i)
    return "·".join(useful_elements)
