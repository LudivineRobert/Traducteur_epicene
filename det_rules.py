#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:21:01 2019

@author: Ludivine
"""
import re

text= "le publiciste"
#text= "un publiciste"
#text= "du publiciste"
#text= "ce publiciste"
#text= "mon publiciste"
#text= "ton publiciste"
#text= "son publiciste"
#text= "quel publiciste"
#text= "quels publicistes"
#text= "aucun publiciste"
#text= "aucuns publicistes"
#text= "nul publiciste"
#text= "nuls publicistes"
#text= "tout publicistes"
#text= "certains publicistes"
#text= "divers publicistes"
#text= "différents publiciste"


defini= re.sub(r"\b([Ll]e|[Ll]a)\b","l•e•a",text)
print(defini)

indefini= re.sub(r"\b(un|une)\b","un•e",text)
print(indefini)

partitif= re.sub(r"\b(du|de l'|de la)\b","d•u•e la",text)
print(partitif)

demonstratif= re.sub(r"\b(ce|cet|cette)\b","ce•tte",text)
print(demonstratif)

possessif1= re.sub(r"\b(mon|ma)\b","m•on•a",text)
print(possessif1)

possessif2= re.sub(r"\b(ton|ta)\b","t•on•a",text)
print(possessif2)

possessif3= re.sub(r"\b(son|sa)\b","s•on•a",text)
print(possessif3)

interrogatifsg= re.sub(r"\b(quel|quelle)\b","quel•le",text)
print(interrogatifsg)

interrogatifpl= re.sub(r"\b(quels|quelles)\b","quel•le•s",text)
print(interrogatifpl)

indefnegatifsg1= re.sub(r"\b(aucun|aucune)\b","aucun•e",text)
print(indefnegatifsg1)

indefnegatifpl1= re.sub(r"\b(aucuns|aucunes)\b","aucun•e•s",text)
print(indefnegatifpl1)

indefnegatifsg2= re.sub(r"\b(nul|nulle)\b","nul•le",text)
print(indefnegatifsg2)

indefnegatifpl2= re.sub(r"\b(nuls|nulles)\b","nul•le•s",text)
print(indefnegatifpl2)

indeftotalite= re.sub(r"\b(tout|toute)\b","tout•e•s",text)
print(indeftotalite)

indefpluralite1= re.sub(r"\b(certains|certaines)\b","certain•e•s",text)
print(indefpluralite1)

indefpluralite2= re.sub(r"\b(divers|diverses)\b","divers•es",text)
print(indefpluralite2)

indefpluralite3= re.sub(r"\b(différents|diférentes)\b","différent•e•s",text)
print(indefpluralite3)
