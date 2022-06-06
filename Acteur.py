# Contient les informations : Nom du personnage, début de l'emploi, fin de l'emploi et cachet
# Un acteur peut avoir joué dnsn plusieurs films (cardinalité : un à plusieurs)

class Acteur:
    "Ceci est la classe Acteur"

    def __init__(self, nompersonnage, debutemploi, finemploi, cachet):
        self._nompersonnage = nompersonnage
        self._debutemploi = debutemploi
        self._finemploi = finemploi
        self._cachet = cachet

    def getNomPersonnage(self):
        return self._nompersonnage
    def getDebutEmploi(self):
        return self._debutemploi
    def getFinEmploi(self):
        return self._finemploi
    def getCachet(self):
        return self._cachet