# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:37:50 2019

@author: rog
"""
import spacy
import os


nlp = spacy.load("fr_core_news_sm")

#Créer une liste pour y mettre les noms de fichier
#Ouvrir les fichiers
#Parcourir la variable (fichier) et mettre les mots dans une liste
#Comparer les élements dans la liste output traducteur et output 

def nettoyage(doc ,file):
    symboles = ("«", "»", ":" , "!" , "%", "(", ")", "’", '.', ',',"—", '-', '"', '?',';','+', "'", "¨", "/", "€", "°", '"',"\n","\t" )
    
    with open('./'+doc+'/'+file, 'r', encoding='UTF-8') as doc:
        data = doc.read()
        
        for e in symboles :
            data = data.replace(e, ' ')
            
        data = data.split(' ')
        
        while "" in data:
            data.remove('')
        
    return list(data)

#print(nettoyage('expected_outputs', 'agriculteurs.txt'))
#=============================================================================
for elem in os.listdir('./inputs'):
    if not os.path.isdir(elem):
        print("'%s' un fichier" % elem)
    if elem.endswith(".txt"):
        #if elem not in ("agriculteurs.txt","eco.txt"): #Still have problems with agriculteurs.txt and eco.txt
        words_input = nlp(' '.join(nettoyage('inputs', elem)))
        words_output = nlp(' '.join(nettoyage('outputs', 'epicene_'+elem)))
        words_expected = nlp(' '.join(nettoyage('expected_outputs', elem)))
        
        
        print("input",len(words_input), "output",len(words_output), "expected", len(words_expected))
        #print("wesh", words_input[0].text)
        #capital.txt, critique_film.txt, peguy.txt, offre_emploi.txt hopital.txt, dialogue.txt
        """
        for e in range(len(words_input)):
            word = words_input[e]
            
            if word != words_expected[e] and words_output[e] == words_expected[e]:
                print(words_output[e])
            
            elif e != words_expected[word] and words_output[word] == words_expected[word]:
                print(e)
        print(words_input)
        print(words_output)
        print(words_expected)"""