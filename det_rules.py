#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def epicenize_det(det):
    """
    Takes a determinant string,
    returns its epicenized form
    """
    # defini
    det = re.sub(r"\bl[ea]\b", "l·e·a", det)
    # indefini
    det = re.sub(r"\bune?\b", "un·e", det)
    # partitif
    det = re.sub(r"\bd(u|e\sla)\b", "d·u·e la", det)
    det = re.sub(r"\bde\sl'", "d·u·e l'", det)
    # ddemonstratif
    det = re.sub(r"\b(ce|cet|cette)\b", "ce·tte", det)
    # dpossessif1
    det = re.sub(r"\b(mon|ma)\b", "m·on·a", det)
    # dpossessif2
    det = re.sub(r"\b(ton|ta)\b", "t·on·a", det)
    # dpossessif3
    det = re.sub(r"\b(son|sa)\b", "s·on·a", det)
    # interrogatifsg
    det = re.sub(r"\b(quel|quelle)\b", "quel·le", det)
    # interrogatifpl
    det = re.sub(r"\b(quels|quelles)\b", "quel·le·s", det)
    # indefnegatifsg1
    det = re.sub(r"\b(aucun|aucune)\b", "aucun·e", det)
    # indefnegatifpl1
    det = re.sub(r"\b(aucuns|aucunes)\b", "aucun·e·s", det)
    # indefnegatifsg2
    det = re.sub(r"\b(nul|nulle)\b", "nul·le", det)
    # indefnegatifpl2
    det = re.sub(r"\bnul(s|es)\b", "nul·le·s", det)
    # dindeftotalite
    det = re.sub(r"\b(tout|toutes)\b", "tout·e·s", det)
    # indefpluralite1
    det = re.sub(r"\bcertain(s|es)\b", "certain·e·s", det)
    # indefpluralite2
    det = re.sub(r"\bdiver(s|ses)\b", "divers·es", det)
    # indefpluralite3
    det = re.sub(r"\bdifférent(s|es)\b", "différent·e·s", det)
    return det


def epicenize_pron(pron):
    """
    Takes a pronoun string,
    returns its epicenized form
    """
    # pronomsg
    pron = re.sub(r"\b(il|elle)\b", "iel", pron)
    # pronompl
    pron = re.sub(r"\b(ils|elles)\b", "iels", pron)
    # pdemonstratif
    pron = re.sub(r"\b(celui|celle)\b", "cel·ui·le", pron)
    # ppossessif1
    pron = re.sub(r"\b(le\smien|la\smienne)\b", "l·e·a mien·ne", pron)
    # ppossessif2
    pron = re.sub(r"\b(le\stien|la\stienne)\b", "l·e·a tien·ne", pron)
    # ppossessif3
    pron = re.sub(r"\b(le\ssien|la\ssienne)\b", "l·e·a sien·ne", pron)
    # ppossessif4
    pron = re.sub(r"\b(le\snôtre|la\snôtre)\b", "l·e·a nôtre", pron)
    # ppossessif5
    pron = re.sub(r"\b(le\svôtre|la\svôtre)\b", "l·e·a vôtre", pron)
    # ppossessif6
    pron = re.sub(r"\b(le\sleur|la\sleur)b", "l·e·a leur", pron)
    # pindefsingularite
    pron = re.sub(r"\b(chacun|chacune)\b", "chacun·e", pron)
    # pindefpluralite
    pron = re.sub(r"\b(certains|certaines)\b", "certain·e·s", pron)
    # pindeftotalite
    pron = re.sub(r"\b(tous|toutes)\b", "tou·te·s", pron)
    return pron
