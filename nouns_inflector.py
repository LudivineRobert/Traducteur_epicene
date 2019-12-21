#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('Morphalou/commonNoun_Morphalou3.1_LMF.xml')
root = tree.getroot()


def get_lexical_entry(orthography):
    """
    Takes the orthographic form of a noun,
    returns its xml entry in the morphalou file
    """
    for element in tree.findall('./lexicalEntry'):
        for ortho in element.findall('./formSet/inflectedForm/orthography'):
            if ortho.text == orthography:
                return element
    raise ValueError('Lexical entry not found')


def get_gender(orthography):
    """
    Takes the orthographic form of a noun,
    returns its gender.
    possible values: masculine, feminine, invariant
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        return lexical_entry.find(
            './formSet/lemmatizedForm/grammaticalGender').text
    raise ValueError('Noun not found')


def get_feminine(orthography):
    """
    Takes the orthographic form of a masculine noun,
    returns its feminine gendered form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        gender = get_gender(orthography)
        if gender == 'masculine':
            for element in tree.findall('./lexicalEntry'):
                if element.find('./feminineVariantOf') is not None:
                    if element.find(
                            './feminineVariantOf').get('target') == \
                            lexical_entry.get('id'):
                        return element.find(
                            './formSet/lemmatizedForm/orthography').text
            raise ValueError('This noun does not allow a feminine form')

        elif gender == 'feminine':
            raise ValueError('This noun is already feminine')
        else:
            raise ValueError('This noun is epicene')
    else:
        raise ValueError('wrong input: word not recognized in the dictionnary')


def get_masculine(orthography):
    """
    Takes the orthographic form of a feminine noun,
    returns its masculine gendered form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        gender = get_gender(orthography)

        if gender == 'feminine':
            if lexical_entry.find('./feminineVariantOf') is not None:
                masculine_id = lexical_entry.find(
                    './feminineVariantOf').get('target')
                for element in root.findall('./lexicalEntry'):
                    if element.get('id') == masculine_id:
                        return element.find(
                            './formSet/lemmatizedForm/orthography').text
            else:
                raise ValueError('This noun does not allow a masculine form')
        elif gender == 'masculine':
            raise ValueError('Noun already masculine')
        else:
            raise ValueError('This noun is epicene')
    else:
        raise ValueError('wrong input: word not recognized in the dictionnary')


def get_number(orthography):
    """
    Takes the orthographic form of a noun,
    return its grammatical number.
    possible values: singular, plural, invariant.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalNumber').text
    raise ValueError('word not found')


def pluralize(orthography):
    """
    Takes the orthographic form of a singular noun,
    return its plural form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'plural':
            raise ValueError('Adjective already plural')
        if number == 'invariable':
            raise ValueError(
                'Noun invariable in number when {}'.format(gender))
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./grammaticalNumber').text == 'plural':
                return inflexion.find('orthography').text
    raise ValueError('word not found')


def singularize(orthography):
    """
    Takes the orthographic form of a plural noun,
    return its singular form.
    """
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry is not None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'singular':
            raise ValueError('Adjective already singular')
        if number == 'invariable':
            raise ValueError(
                'Noun invariable in number when {}'.format(gender))
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./grammaticalNumber').text == 'singular':
                return inflexion.find('orthography').text
    raise ValueError('word not found')
