class Voyante(object):
    """docstring for Voyante."""
    def __init__(self):
        super(Voyante, self).__init__()

    def devoile(self):
        return ("Voyante");

    async def pouvoir(self, partie):
        partie.prochainRole="Voyante"
        await partie.interface.afficher(partie.aliveToStr())
        await partie.interface.afficher("Sonder qui (index): ")
        choix = await partie.interface.faireChoix(partie.alive)
        await partie.interface.afficher("La voyante a sonde un " + choix.role.devoile())
