# (Hérite de la classe Personne)
# Contient les informations : Date d'embauche, code utilisateur, password et type d'accès

class Employe:
    "Ceci est la classe Employe"

    def __init__(self, dateembauche, codeutilisateur, passwordemploye, typeacces):
        self._dateembauche = dateembauche
        self._codeutilisateur = codeutilisateur
        self._passwordemploye = passwordemploye
        self._typeacces = typeacces

    def getDateEmbauche(self):
        return self._dateembauche
    def getCodeUtilisateur(self):
        return self._codeutilisateur
    def getPasswordEmploye(self):
        return self._passwordemploye
    def getTypeAcces(self):
        return self._typeacces


def __str__(self):
        return "La date d'embauche est {}, le code utilisateur est {}, le mot de passe est {} et le type d'accès est {}".format(self._dateembauche, self._codeutilisateur, self._password, self.typeacces)

