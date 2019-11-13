import xml.etree.ElementTree as ET

tree = ET.parse('Morphalou/commonNoun_Morphalou3.1_LMF.xml')
root = tree.getroot()

def search(lemma):
    for element in root.findall('./lexicalEntry'):
        if lemma in element.attrib['id']:
            return element
    return None