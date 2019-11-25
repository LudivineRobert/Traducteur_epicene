import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('Morphalou/commonNoun_Morphalou3.1_LMF.xml')
root = tree.getroot()

def get_lexical_entry(orthography):
    for element in tree.findall('./lexicalEntry'):
        for ortho in element.findall('./formSet/inflectedForm/orthography'):
            if ortho.text == orthography:
                return element
    raise ValueError('Lexical entry not found')

def get_gender(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        return lexical_entry.find('./formSet/lemmatizedForm/grammaticalGender').text
    return None


def get_feminine(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        gender = get_gender(orthography)
        if gender == 'masculine':
            #pdb.set_trace()
            for element in tree.findall('./lexicalEntry'):
                if element.find('./feminineVariantOf') != None:
                    if element.find('./feminineVariantOf').get('target')==lexical_entry.get('id'):
                        #pdb.set_trace()
                        return element.find('./formSet/lemmatizedForm/orthography').text
            print('This noun does not allow a feminine form')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
                    
        elif gender == 'feminine':
            print('This noun is already feminine')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
        else:
            print('This noun is epicene')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
    else:
        print('wrong input: word not recognized in the dictionnary')
        return None
    
    
def get_masculine(orthography):
    lexical_entry = get_lexical_entry(orthography)
    #pdb.set_trace()
    if lexical_entry != None:
        gender = get_gender(orthography)
        
        if gender == 'feminine':
            if lexical_entry.find('./feminineVariantOf') != None:
                masculine_id = lexical_entry.find('./feminineVariantOf').get('target')
                for element in root.findall('./lexicalEntry'):
                    if element.get('id') == masculine_id:
                        return element.find('./formSet/lemmatizedForm/orthography').text
            else:
                print('This noun does not allow a masculine form')
                return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
        elif gender == 'masculine':
            print('Noun already masculine')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
        else:
            print('This noun is epicene')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
    else:
        print('wrong input: word not recognized in the dictionnary')
        return None
    
    
def get_number(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./orthography').text == orthography:
                return inflexion.find('./grammaticalNumber').text
            
def pluralize(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'plural':
            print('Adjective already plural')
            return None
        if number == 'invariable':
            print('Noun invariable in number when {}'.format(gender))
            return None
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./grammaticalNumber').text == 'plural':
                return inflexion.find('orthography').text
            
            
def singularize(orthography):
    lexical_entry = get_lexical_entry(orthography)
    if lexical_entry != None:
        number = get_number(orthography)
        gender = get_gender(orthography)
        if number == 'singular':
            print('Adjective already singular')
            return None
        if number == 'invariable':
            print('Noun invariable in number when {}'.format(gender))
            return None
        for inflexion in lexical_entry.findall('./formSet/inflectedForm'):
            if inflexion.find('./grammaticalNumber').text == 'singular':
                return inflexion.find('orthography').text