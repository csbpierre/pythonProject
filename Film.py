# Contient les informations : Nom du film, la durée et une description
# Un film peut avoir plus d'une catégorie (cardinalité : un à plusieurs)

class Film:
    "Ceci est la classe Film"

    def __init__(self, nomfilm, duree, descriptionfilm):
        self._nomfilm = nomfilm
        self._duree = duree
        self._descriptionfilm = descriptionfilm

    def getNomFilm(self):
        return self._nomfilm

    def getDuree(self):
        return self._duree

    def getDescriptionFilm(self):
        return self._descriptionfilm