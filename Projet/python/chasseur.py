#Pas encore en etat de marche
class Chasseur(object):
    """docstring for Chasseur."""
    def __init__(self):
        super(Chasseur, self).__init__()

    def devoile(self):
        return ("Chasseur");

    async def pouvoir(self, partie):
        partie.prochainRole="Chasseur"
        await partie.interface.afficher(str(partie.alive))
        await partie.interface.afficher("Tirer sur qui? (index)")
        choix = await partie.interface.faireChoix(partie.alive)
        await partie.interface.afficher("Le chasseur entraine dans sa mort " + choix.nom)
        await choix.mourir(partie)
        
def str(list):
    l=[]
    for p in list:
        l.append(p.__str__())
    return l