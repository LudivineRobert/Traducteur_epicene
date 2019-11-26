import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('Morphalou/adjective_Morphalou3.1_LMF.xml')
root = tree.getroot()


def get_lexical_entry(orthography):
    #pdb.set_trace()
    for element in tree.findall('./lexicalEntry'):
        for ortho in element.findall('./formSet/inflectedForm/orthography'):
            #pdb.set_trace()
            if ortho.text == orthography:
                return element
    raise ValueError('Lexical entry not found')

def get_gender(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        #pdb.set_trace()
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            #pdb.set_trace()
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalGender').text
    raise ValueError('Word not found')

def get_feminine(orthography):
    if get_gender(orthography) == 'feminine':
        print('Adjective already feminine')
        return None
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            gender = inflexion.find('./grammaticalGender').text
            if gender == 'invariable':
                raise ValueError('Epicene adjective')
            if gender == 'feminine':
                return inflexion.find('./orthography').text

def get_masculine(orthography):
    if get_gender(orthography) == 'masculine':
        raise ValueError('Adjective already masculine')
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            gender = inflexion.find('./grammaticalGender').text
            if gender == 'invariable':
                raise ValueError('Epicene adjective')
            if gender == 'masculine':
                return inflexion.find('./orthography').text
            
            
            
def get_number(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        #pdb.set_trace()
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            #pdb.set_trace()
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalNumber').text
    raise ValueError('Word not found')
    
def pluralize(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'plural':
            raise ValueError('Adjective already plural')
        if number == 'invariable':
            raise ValueError('Adjective invariable in number when {}'.format(gender))
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            number_ = inflexion.find('./grammaticalNumber').text
            gender_ = inflexion.find('./grammaticalGender').text
            if number_ == 'plural' and gender_ == gender:
                return inflexion.find('./orthography').text
    raise ValueError('Word not found')
          
def singularize(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'singular':
            raise ValueError('Adjective already singular')
        if number == 'invariable':
            raise ValueError('Adjective invariable in number when {}'.format(gender))
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            number_ = inflexion.find('./grammaticalNumber').text
            gender_ = inflexion.find('./grammaticalGender').text
            if number_ == 'singular' and gender_ == gender:
                return inflexion.find('./orthography').text
    raise ValueError('Word not found')
    #précieux : number is invariable in masculine but not in feminine