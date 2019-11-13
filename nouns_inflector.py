import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('Morphalou/commonNoun_Morphalou3.1_LMF.xml')
root = tree.getroot()

def get_lexical_entry(lemma):
    for element in tree.findall('./lexicalEntry'):
        if lemma == element.find('./formSet/lemmatizedForm/orthography').text:
            return element
    return None

def get_grammatical_gender(lexical_entry):
    if lexical_entry != None:
        return lexical_entry.find('./formSet/lemmatizedForm/grammaticalGender').text
    return None


def get_feminine_form(lexical_entry):
    if lexical_entry != None:
        gender = get_grammatical_gender(lexical_entry)
        if gender == 'masculine':
            #pdb.set_trace()
            for element in tree.findall('./lexicalEntry'):
                if element.find('./feminineVariantOf') != None:
                    if element.find('./feminineVariantOf').get('target')==lexical_entry.get('id'):
                        #pdb.set_trace()
                        return element.find('./formSet/lemmatizedForm/orthography').text
                    
        elif gender == 'feminine':
            print('This noun is already feminine')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
        else:
            print('This noun is epicene')
            return None
    else:
        print('wrong input: word not recognized in the dictionnary')
        return None
    
    
def get_masculine_form(lexical_entry):
    #pdb.set_trace()
    if lexical_entry != None:
        gender = get_grammatical_gender(lexical_entry)
        
        if gender == 'feminine':
            masculine_id = lexical_entry.find('./feminineVariantOf').get('target')
            for element in root.findall('./lexicalEntry'):
                if element.get('id') == masculine_id:
                    return element.find('./formSet/lemmatizedForm/orthography').text
        elif gender == 'masculine':
            print('Noun already masculine')
            return lexical_entry.find('./formSet/lemmatizedForm/orthography').text
    else:
        print('wrong input: word not recognized in the dictionnary')
        return None
    
    
    
    
    
    
    
    
    