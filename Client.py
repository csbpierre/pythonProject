# (Hérite de la classe Personne)
# Contient les informations : Date d'inscription, courriel, password

class Client:
    """Ceci est la classe Client - Abonnés au service"""

    def __init__(self, dateinscription, courriel, passwordclient):
        self._dateinscription = dateinscription
        self._courriel = courriel
        self._passwordclient = passwordclient
    def getDateInscription(self):
        return self._nom
    def getCourriel(self):
        return self._courriel
    def getPasswordClient(self):
        return self._passwordclient