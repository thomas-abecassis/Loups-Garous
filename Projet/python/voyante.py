class Voyante(object):
    """docstring for Voyante."""
    def __init__(self):
        super(Voyante, self).__init__()

    def devoile(self):
        return ("Voyante");

    async def pouvoir(self, partie):
        partie.prochainRole="Voyante"
        await partie.interface.afficherAUnRole(partie.aliveToStr(),self)
        await partie.interface.afficherAUnRole("Sonder qui (index): ",self)
        choix = await partie.interface.faireChoix(partie.alive,partie.JoueursAvecRole(self))
        await partie.interface.afficherAUnRole("La voyante a sonde un " + choix.role.devoile(),self)
