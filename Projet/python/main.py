import partie as p
import intCons as IC

import asyncio

interface = IC.IntCons()
joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet", "Arnaud"]
role = ["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
partie = p.Partie(interface, joueur, role)

loop = asyncio.get_event_loop()

loop.run_until_complete(partie.playGame())

