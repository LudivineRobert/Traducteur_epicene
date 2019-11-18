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

#determinant part
defini= re.sub(r"\b([Ll]e|[Ll]a)\b","l•e•a",text)
print(defini)

indefini= re.sub(r"\b(un|une)\b","un•e",text)
print(indefini)

partitif= re.sub(r"\b(du|de l'|de la)\b","d•u•e la",text)
print(partitif)

ddemonstratif= re.sub(r"\b(ce|cet|cette)\b","ce•tte",text)
print(ddemonstratif)

dpossessif1= re.sub(r"\b(mon|ma)\b","m•on•a",text)
print(dpossessif1)

dpossessif2= re.sub(r"\b(ton|ta)\b","t•on•a",text)
print(dpossessif2)

dpossessif3= re.sub(r"\b(son|sa)\b","s•on•a",text)
print(dpossessif3)

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

dindeftotalite= re.sub(r"\b(tout|toute)\b","tout•e•s",text)
print(dindeftotalite)

indefpluralite1= re.sub(r"\b(certains|certaines)\b","certain•e•s",text)
print(indefpluralite1)

indefpluralite2= re.sub(r"\b(divers|diverses)\b","divers•es",text)
print(indefpluralite2)

indefpluralite3= re.sub(r"\b(différents|diférentes)\b","différent•e•s",text)
print(indefpluralite3)

#pronouns part
pronomsg= re.sub(r"\b(il|elle)\b","iel",text)
print(pronomsg)

pronompl= re.sub(r"\b(ils|elles)\b","iels",text)
print(pronompl)

pdemonstratif= re.sub(r"\b(celui|celle)\b","cel•ui•le",text)
print(pdemonstratif)

ppossessif1= re.sub(r"\b(le mien|la mienne)\b","l•e•a mien•ne",text)
print(ppossessif1)

ppossessif2= re.sub(r"\b(le tien|la tienne)\b","l•e•a tien•ne",text)
print(ppossessif2)

ppossessif3= re.sub(r"\b(le sien|la sienne)\b","l•e•a sien•ne",text)
print(ppossessif3)

ppossessif4= re.sub(r"\b(le nôtre|la nôtre)\b","l•e•a nôtre",text)
print(ppossessif4)

ppossessif5= re.sub(r"\b(le vôtre|la vôtre)\b","l•e•a vôtre",text)
print(ppossessif5)

ppossessif6= re.sub(r"\b(le leur|la leur)\b","l•e•a leur",text)
print(ppossessif6)

pindefsingularite= re.sub(r"\b(chacun|chacune)\b","chacun•e",text)
print(pindefsingularite)

pindefpluralite= re.sub(r"\b(certains|certaines)\b","certain•e•s",text)
print(pindefpluralite)

pindeftotalite= re.sub(r"\b(tous|toutes)\b","tou•te•s",text)
print(pindeftotalite)

