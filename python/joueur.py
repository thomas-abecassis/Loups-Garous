import random
import lg
import sv

class Joueur(object):
    """docstring for Joueur."""
    def __init__(self, nom, role):
        super(Joueur, self).__init__()
        self.nom = nom
        if (role == "LG"):
            self.role = lg.LoupGarou()
        else:
            self.role = sv.SV()
        self.vivant = True

    def __repr__(self):
        return (self.__str__())

    def __str__(self):
        return (self.nom)

    def printJoueur(self):
        print ("Je suis", self.nom, "et je suis un(e)", self.role.__class__.__name__)

    def mourir(self):
        print(self.nom + " est mort et il etait " + self.role.__class__.__name__)
        self.vivant = False

    def voter(self, vivant):
        print(vivant)
        choix = int(input("Voter contre (index): "))
        while (choix >= len(vivant) or choix < 0):
            choix = int(input("Voter contre (index): "))
        mort = vivant[choix]
        print(self.nom + " a vote contre " + mort.nom)
        return (mort)
