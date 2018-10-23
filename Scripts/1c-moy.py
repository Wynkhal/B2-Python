#! C:/Users/Valentin/AppData/Local/Programs/Python/Python36-32/python.exe
#1c-moy
#Script permettant d'ajouter des prénoms et des notes à une liste et de sortir une moyenne ainsi que me top 5
#Raffy Valentin
#15/10/2018
import operator

def convertInt(param):
    try:
        return int(param)
    except ValueError:
        return -1

dico = {}

print('Veuillez entrer un prénom et une note (séparés par un espace).')

#Boucle permettant de vérifier les entrées utilisateurs
while True:
    read = input('')

    if read == "q":
        break

    read = str(read).split(' ')

    if len(read) < 2:
        print("Êtes-vous sûr d'avoir mis un espace ?")
        continue

    nom = read[0]
    note = convertInt(read[1])
    
    if note == -1:
        print("Avez-vous vraiment entré une note ?")
        continue

    if nom in dico:
        print("Vous avez déjà mis une note pour " + nom)
        continue

    dico[nom] = note

#Permet de retourner et afficher les 5 meilleurs moyennes
moyenne = sum(dico.values()) / float(len(dico))
print("Moyenne: " + moyenne)
print(sorted(dico.items(), key=operator.itemgetter(1), reverse = True)[:5])



