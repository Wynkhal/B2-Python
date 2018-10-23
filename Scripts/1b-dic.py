#! C:/Users/Valentin/AppData/Local/Programs/Python/Python36-32/python.exe
#1b-dic
#Script permettant d'ajouter des prénoms à une liste et de les sortir par ordre alphabétique
#Raffy Valentin
#15/10/2018
import re
prenom = input("Entez un Prénom : (Appuyer sur Q pour quitter)")

# On importe la condition
pattern = re.compile("^[^0-9]+$")
listePrenom = []

# Fonction pour ajouter des prénoms à la liste puis les afficher
def ajouterPrenom(prenom):
        while prenom != "q" :
            if (pattern.match(prenom)):
                listePrenom.append(prenom)
                prenom = input ("Entrez un Prénom, ou appuyer sur Q pour quitter : ")
            else: 
                prenom = input ("Entrez un Prénom correct : ")

        listePrenom.sort()

        print('\nVoici la liste des prénoms :')
        for prenom in listePrenom:
            print (prenom)

ajouterPrenom(prenom)

input ("Appuyer sur une touche pour quitter.")
