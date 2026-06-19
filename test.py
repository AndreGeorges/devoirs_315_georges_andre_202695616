
mesures = [ {"type": "temp", "valeur": 21.4},{"type": "temp", "valeur": 17.6}  ] 

def etat_capteur(valeur, seuil_min, seuil_max):
    if valeur >= seuil_max+10 or valeur<= seuil_min-10:
        print(f"{valeur} est un état critique")
    elif valeur <= seuil_min: 
        print(f"{valeur} est un état bas")
    elif valeur >= seuil_max:
        print(f"{valeur} est un état élevé")
    else:
        print(f"{valeur} est un état moyen")
    
# renvoie la moyenne des nombres contenus dans liste. Vous devez accumuler la 
# somme dans une boucle (sans utiliser de fonction toute faite qui calcule la moyenne). 
def moyenne(liste: list[float]):
    total = 0
    if len(liste) == 0:
        return 0
    for valeur in liste:
        total += valeur
    moyenne = total / len(liste)
    return moyenne

# reçoit une liste de mesures, où chaque mesure est un dictionnaire
# La fonction extrait la valeur de chaque mesure (mesure["valeur"]), les regroupe dans une liste, puis 
# délègue le calcul à moyenne. Vous réutilisez ainsi votre première fonction au lieu de réécrire la logique. 
def moyenne_mesures(mesures: list[dict[str, float]]) :    
    liste = []
    for m in mesures:
        liste.append(m["valeur"])
    return liste


# Combine deux entrées pour renvoyer une appréciation du confort, par exemple : 
# • "confortable", "trop sec", "trop humide", "inconfortable".
def niveau_confort(temp, humidite):
    etat = ""
    if temp < 20: 
        etat += "trop froid "
    if temp > 22:
        etat += "trop chaud "
    if humidite < 30:
        etat += "trop sec "
    if humidite > 50:
        etat += "trop humide "
    else: 
        etat += "confortable "
    return etat
    
def affichage( etat):
    print("===========AFFICHAGE==============")
    print("Type", "Valeur", "etat")
    print(etat)

# print(etat_capteur(5, 17, 25))
# print(moyenne([1.5,4,6.5]))
# print(moyenne_mesures([ {"type": "temp", "valeur": 21.4},{"type": "temp", "valeur": 17.6}  ]))
# print(moyenne(moyenne_mesures(  mesures )))
print(niveau_confort(19, 60))
# print(affichage( etat_capteur(5, 17, 25))) 


 