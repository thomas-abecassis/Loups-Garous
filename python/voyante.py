class Voyante(object):
    """docstring for Voyante."""
    def __init__(self):
        super(Voyante, self).__init__()

    def devoile(self):
        return ("Voyante");

    def pouvoir(self, alive):
        print(alive)
        choix = int(input("Sonder (index): "))
        while (choix >= len(alive) or choix < 0):
            choix = int(input("Sonder (index): "))
        sonde = alive[choix]
        print("La voyante a sonde un " + sonde.role.devoile())
