# Contient les informations de base : Nom et prénom de la personne, Genre

class Personne:
    "Ceci est la classe personne"

    def __init__(self, nom, prenom, genre):
        self._nom = nom
        self._prenom = prenom
        self._genre = genre
    def getnom(self):
        return self._nom
    def getprenom(self):
        return self._prenom
    def getgenre(self):
        return self._genre


# (Classe Client, Hérite de la classe Personne)
# Contient les informations : Date d'inscription, courriel, password

class Client(Personne):
    """Ceci est la classe Client - Abonnés au service"""

    def __init__(self, nom, prenom, genre, dateinscription, courriel, passwordclient):
        Personne.__init__(nom, prenom, genre)
        self._dateinscription = dateinscription
        self._courriel = courriel
        self._passwordclient = passwordclient

    def getdateinscription(self):
        return self._dateinscription
    def getcourriel(self):
        return self._courriel
    def getpasswordclient(self):
        return self._passwordclient


# (Classe Acteur, Hérite de la classe Personne)
# Contient les informations : Nom du personnage, début de l'emploi, fin de l'emploi et cachet
# Un acteur peut avoir joué dans plusieurs films (cardinalité : un à plusieurs)

class Acteur(Personne):
    "Ceci est la classe Acteur"

    def __init__(self, nom, prenom, genre, nompersonnage, debutemploi, finemploi, cachet):
        Personne.__init__(nom, prenom, genre)
        self._nompersonnage = nompersonnage
        self._debutemploi = debutemploi
        self._finemploi = finemploi
        self._cachet = cachet

    def getnompersonnage(self):
        return self._nompersonnage
    def getdebutemploi(self):
        return self._debutemploi
    def getfinemploi(self):
        return self._finemploi
    def getcachet(self):
        return self._cachet


# (Classe Employe, Hérite de la classe Personne)
# Contient les informations : Date d'embauche, code utilisateur, password et type d'accès

class Employe(Personne):
    "Ceci est la classe Employe"

    def __init__(self, nom, prenom, genre, dateembauche, codeutilisateur, passwordemploye, typeacces):
        Personne.__init__(nom, prenom, genre)
        self._dateembauche = dateembauche
        self._codeutilisateur = codeutilisateur
        self._passwordemploye = passwordemploye
        self._typeacces = typeacces

    def getdateembauche(self):
        return self._dateembauche
    def getcodeutilisateur(self):
        return self._codeutilisateur
    def getpasswordemploye(self):
        return self._passwordemploye
    def gettypeacces(self):
        return self._typeacces



# Définition d'entrées satiques pour les besoins de la mise en situation
p1 = Personne("Gagnon", "Pierre", "Masculin")
p2 = Personne("Delauniere", "Josee", "Feminin")
p3 = Personne("Gagnon", "Rose", "Feminin")
p4 = Personne("Lavoie", "Maxim", "Feminin")

#print (p1.getnom(),p1.getprenom(),p1.getgenre())
#print (p2.getnom(),p2.getprenom(),p2.getgenre())
#print (p3.getnom(),p3.getprenom(),p3.getgenre())
#print (p4.getnom(),p4.getprenom(),p4.getgenre())

#print(p4.getgenre())

e1 = Employe("Gagnon", "Pierre", "Masculin", "2022-01-01", "gagnon.pierre", "login123", "FullAccess")
e2 = Employe("Gagnon", "Rose", "Feminin", "2022-02-02", "gagnon.rose", "login123", "ReadOnly")
e3 = Employe("Gagnon", "Karole", "Feminin", "2022-03-03", "gagnon.karole", "login123", "FullAccess")
e4 = Employe("Gagnon", "Paul", "Masculin", "2022-04-04", "gagnon.paul", "login123", "ReadOnly")

#print (e1.getdateembauche(),e1.getcodeutilisateur(),e1.getpassword(),e1.gettypeacces())
#print (e2.getdateembauche(),e2.getcodeutilisateur(),e2.getpassword(),e2.gettypeacces())
#print (e3.getdateembauche(),e3.getcodeutilisateur(),e3.getpassword(),e3.gettypeacces())
#print (e4.getdateembauche(),e4.getcodeutilisateur(),e4.getpassword(),e4.gettypeacces())
