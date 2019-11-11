import random
import lg
import sv
import voyante as vovo
import chasseur

class Joueur(object):
    """docstring for Joueur."""
    def __init__(self, nom, role):
        super(Joueur, self).__init__()
        self.nom = nom
        if (role == "LG"):
            self.role = lg.LoupGarou()
        elif (role == "Voyante"):
            self.role = vovo.Voyante()
        elif (role=="Chasseur"):
            self.role= chasseur.Chasseur()
        else:
            self.role = sv.SV()
        self.vivant = True

    def __repr__(self):
        return (self.__str__())

    def __str__(self):
        return (self.nom)

    async def printJoueur(self, partie):
        await partie.interface.afficher("Je suis " + self.nom + " et je suis un(e) " + self.role.devoile())

    async def mourir(self, partie):
        await partie.interface.afficher(self.nom + " est mort et il etait " + self.role.devoile())
        self.vivant = False
        partie.interface.mettreAJour(partie)
        if self.role.devoile() == "Chasseur":
            await self.role.pouvoir(partie)

    async def voter(self, partie, list):
        await partie.interface.afficher(str(list))
        await partie.interface.afficher("Voter contre (index): ")
        choix = await partie.interface.faireChoix(list)
        await partie.interface.afficher(self.nom + " a vote contre " + choix.nom)
        return (choix)
    
def str(list):
    l=[]
    for p in list:
        l.append(p.__str__())
    return l
