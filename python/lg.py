import role

class LoupGarou(object):
    """docstring for LoupGarou."""
    def __init__(self):
        super(LoupGarou, self).__init__()

    def manger(self,nom, vill):
        print(vill)
        choix = int(input("Voter contre (index): "))
        while (choix >= len(vill) or choix < 0):
            choix = int(input("Voter contre (index): "))
        mort = vill[choix]
        print(nom + " veux manger " + mort.nom)
        return (mort)

    def devoile(self):
        return ("Loup-Garou");

    def pouvoir(self):
        pass
