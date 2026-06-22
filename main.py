# Dans un fichier principal, écrivez un court programme qui met vos fonctions en scène : 
# 1. Simulez 2 capteurs (par exemple température et humidité) sur 20 mesures. Les valeurs doivent 
# varier d’une mesure à l’autre (et non rester constantes). 
# 2. Stockez chaque mesure dans un dictionnaire (type, valeur), et conservez l’ensemble dans 
# deux listes. 
# 3. Pour chaque mesure, affichez son état à l’aide de etat_capteur(). 
# 4. À la fin, affichez la moyenne de chaque capteur avec moyenne_mesures(), puis une 
# appréciation globale du confort avec niveau_confort().
import random
from test import etat_capteur, moyenne, moyenne_mesures, niveau_confort, affichage

def creer_random_temperatures():
    temperatures = []
    
    for i in range(20):
        temp = random.randint(1000,3000)/100
        
        temperature = {
            "type": "temperature",
            "valeur" : temp,
        }
        
        temperatures.append(temperature)
        
    return temperatures

def creer_random_humidites():
    humidites = []
    
    for i in range(20):
        hum =  random.randint(2000, 8000)/100
        
        humidite = {
            "type": "humidite",
            "valeur" : hum,
        }
        
        humidites.append(humidite)
        
    return humidites

# ============== AFFFICHAGE ================

temperatures = creer_random_temperatures()

for t in temperatures: 
    print(etat_capteur(t["valeur"], 17, 25))
    
humidites = creer_random_humidites()

for h in humidites:
    print(etat_capteur(h["valeur"], 30, 60 ))

t = moyenne(moyenne_mesures(creer_random_temperatures()))
print(t)
h = moyenne(moyenne_mesures(creer_random_humidites()))
print(h)

print(niveau_confort(t, h))
    