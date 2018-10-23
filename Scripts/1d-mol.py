#! C:\Users\Valentin\AppData\Local\Programs\Python\Python36-32\python.exe
# 1d-mol
# Description : Création d'un jeu du plus ou moins
# Auteur : RAFFY Valentin
# Date : 23/10/2018

import re
import random
import signal
import sys
from time import sleep

print('Jeu du Plus ou Moins\n')
print("Vous devez trouver le nombre étant compris entre 0 et 100")
pattern = re.compile("[0-9]+$")
print("(Entrez 'q' pour quitter)\n")

nbAleatoire = random.randint(0, 100) # Genere un nombre aléatoire entre 0 et 100
nbCoups = 0
print(nbAleatoire)

# Fonctions du permettant le fonctionnement du Plus ou Moins
def plusOuMoins(nbUtilisateur, nbCoups):
    while(nbUtilisateur != "q"):
        if(pattern.match(nbUtilisateur)): # verification d'une saisie correct
            if(int(nbUtilisateur) > nbAleatoire):
                print("C'est moins")
                nbCoups += 1
                nbUtilisateur = input("Entrez un nombre : ")
            elif(int(nbUtilisateur) < nbAleatoire):
                print("C'est plus")
                nbCoups += 1
                nbUtilisateur = input("Entrez un nombre : ")
            else:
                nbCoups += 1
                print("\nFélicitation ! Vous avez trouvé en "+str(nbCoups)+" coups.")
                resultat()
                break 
        else:
            print("Saisie invalide") #erreur retourné quand un caractère autre que int est rentré
            nbUtilisateur = input("Entrez un nombre valide : ")
    if(nbUtilisateur == "q"):
        resultat()


# Fonction marquant la fin du programme lors du signal CTRL+C
def fin(signal, frame):
    resultat()
    sleep(1)
    sys.exit(0)

# Fonction qui affiche le résultat avant la fermeture du jeu  
def resultat():
    print("\nLa solution était "+str(nbAleatoire))
    print("Au revoir !")

signal.signal(signal.SIGINT, fin)

nbUtilisateur = input("Entrez un nombre : ") # saisie utilisateur
plusOuMoins(nbUtilisateur,nbCoups)