# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#if __name__ == "__main__":
    #c1 = CarteCredit.CarteCredit("Visa", 132456789)
    #c2 = CarteCredit.CarteCredit("MasterCard", 132456789)

    #p1 = Personne.Personne("Couture", "Robert", 1998)
    #p1.ajoutCarteCredit(c1)
    #p1.ajoutCarteCredit(c2)

    #for carte in p1.getListeCartesCredit():
    #    print(carte)

#listeCartes = p1.getListeCartesCredit()
#for carte in listeCartes:
#    print(carte.getType())

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# From SignauxPythonQT-main
# Pour Interface Graphique avec Login
# Contient les informations de base : Nom et prénom de la personne, Genre

###########################################################################

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
        Personne.__init__(self, nom, prenom, genre)
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
        Personne.__init__(self, nom, prenom, genre)
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
        Personne.__init__(self, nom, prenom, genre)
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

e1 = Employe("Gagne", "Pierre", "Masculin", "2022-01-01", "gagne.pierre", "login123", "FullAccess")
e2 = Employe("Gagnon", "Rose", "Feminin", "2022-02-02", "gagnon.rose", "login123", "ReadOnly")
e3 = Employe("Gagnon", "Karole", "Feminin", "2022-03-03", "gagnon.karole", "login123", "FullAccess")
e4 = Employe("Gagnon", "Paul", "Masculin", "2022-04-04", "gagnon.paul", "login123", "ReadOnly")

#print (e1.getdateembauche(),e1.getcodeutilisateur(),e1.getpassword(),e1.gettypeacces())
#print (e2.getdateembauche(),e2.getcodeutilisateur(),e2.getpassword(),e2.gettypeacces())
#print (e3.getdateembauche(),e3.getcodeutilisateur(),e3.getpassword(),e3.gettypeacces())
#print (e4.getdateembauche(),e4.getcodeutilisateur(),e4.getpassword(),e4.gettypeacces())






######################################################################

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp


class Ui_fen2(QtWidgets.QWidget):
    def __init__(self, employe):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Fen2")
        self.resize(371, 183)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(qApp.quit)
        self.labelNom = QtWidgets.QLabel(self)
        self.labelNom.setGeometry(QtCore.QRect(20, 10, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelNom.setFont(font)
        self.labelNom.setObjectName("labelNom")
        self.setWindowTitle("Dialog")
        self.labelNom.setText("Usager: " + employe)

class Ui_fen1(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def verification(self):
        if self.txtUsager.text() == 'gagnon.pierre':
            if self.txtMotPasse.text() == "login123":
                self.switch_window.emit(self.txtUsager.text())


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Fen1")
        self.resize(371, 183)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(self.verification)
        self.txtUsager = QtWidgets.QLineEdit(self)
        self.txtUsager.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.txtUsager.setObjectName("txtUsager")
        self.txtMotPasse = QtWidgets.QLineEdit(self)
        self.txtMotPasse.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.txtMotPasse.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtMotPasse.setObjectName("txtMotPasse")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(36, 100, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.setWindowTitle( "Dialog")
        self.label.setText( "Usager")
        self.label_2.setText("Mot de passe")
        self.label_3.setText( "Fen1")

class Controller:
    def __init__(self):
        pass

    def showFen1(self, *args):
        self.windowF1 = Ui_fen1()
        self.windowF1.switch_window.connect(self.showFen2)
        self.windowF1.show()


    def showFen2(self, user, *args): #Args permet d'ajouter ce que l'on veut. Ici c'est le str du signal
        self.windowF2 = Ui_fen2(user)
        self.windowF1.close()
        self.windowF2.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showFen1()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()