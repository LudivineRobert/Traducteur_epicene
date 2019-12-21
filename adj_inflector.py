#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('Morphalou/adjective_Morphalou3.1_LMF.xml')
root = tree.getroot()


def get_lexical_entry(orthography):
    """
    Takes the orthographic form of an adjective,
    returns its xml entry in the morphalou file
    """
    for element in tree.findall('./lexicalEntry'):
        for ortho in element.findall('./formSet/inflectedForm/orthography'):
            if ortho.text == orthography:
                return element
    raise ValueError('Lexical entry not found')


def get_gender(orthography):
    """
    Takes the orthographic form of an adjective,
    returns its gender.
    possible values: masculine, feminine, invariant
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalGender').text
    raise ValueError('Word not found')


def get_feminine(orthography):
    """
    Takes the orthographic form of a masculine adjective,
    returns its feminine gendered form.
    """
    if get_gender(orthography) == 'feminine':
        print('Adjective already feminine')
        return None
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            gender = inflexion.find('./grammaticalGender').text
            if gender == 'invariable':
                raise ValueError('Epicene adjective')
            if gender == 'feminine':
                return inflexion.find('./orthography').text


def get_masculine(orthography):
    """
    Takes the orthographic form of a feminine adjective,
    returns its masculine gendered form.
    """
    if get_gender(orthography) == 'masculine':
        raise ValueError('Adjective already masculine')
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            gender = inflexion.find('./grammaticalGender').text
            if gender == 'invariable':
                raise ValueError('Epicene adjective')
            if gender == 'masculine':
                return inflexion.find('./orthography').text


def get_number(orthography):
    """
    Takes the orthographic form of an adjective,
    return its grammatical number.
    possible values: singular, plural, invariant.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalNumber').text
    raise ValueError('Word not found')


def pluralize(orthography):
    """
    Takes the orthographic form of a singular adjective,
    return its plural form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'plural':
            raise ValueError('Adjective already plural')
        if number == 'invariable':
            print('Adjective invariable in number when {}'.format(gender))
            return orthography
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            number_ = inflexion.find('./grammaticalNumber').text
            gender_ = inflexion.find('./grammaticalGender').text
            if number_ == 'plural' and gender_ == gender:
                return inflexion.find('./orthography').text
    raise ValueError('Word not found')


def singularize(orthography):
    """
    Takes the orthographic form of a plural adjective,
    return its singular form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'singular':
            raise ValueError('Adjective already singular')
        if number == 'invariable':
            print('Adjective invariable in number when {}'.format(gender))
            return orthography
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            number_ = inflexion.find('./grammaticalNumber').text
            gender_ = inflexion.find('./grammaticalGender').text
            if number_ == 'singular' and gender_ == gender:
                return inflexion.find('./orthography').text
    raise ValueError('Word not found')
