#Pas encore en etat de marche
class Chasseur(object):
    """docstring for Chasseur."""
    def __init__(self):
        super(Chasseur, self).__init__()

    def devoile(self):
        return ("Chasseur");

    async def pouvoir(self, partie):
        partie.prochainRole="Chasseur"
        await partie.interface.afficherAUnRole(str(partie.alive),self)
        await partie.interface.afficherAUnRole("Tirer sur qui? (index)",self)
        choix = await partie.interface.faireChoix(partie.alive,partie.JoueursAvecRole(self))
        await partie.interface.afficherAUnRole("Le chasseur entraine dans sa mort " + choix.nom,self)
        await choix.mourir(partie)
        
def str(list):
    l=[]
    for p in list:
        l.append(p.__str__())
    return l
