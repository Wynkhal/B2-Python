#! C:\Users\Valentin\AppData\Local\Programs\Python\Python36-32\python.exe
# 2a-mol
# Description : Création d'un jeu du plus ou moins, avec lecture et écriture dans un fichier
# Auteur : RAFFY Valentin
# Date : 05/11/2018



#On importe le module "signal"
import signal


#On importe le module "random"
import random


#On importe le module "re"
import re


#On défini les variables dont on a besoin
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
end = False
print(solution)

#On créé la fonction de fin

def fin():
     print("Au revoir, merci d'avoir jouer")
     exit()

#On écrit la fonction permettant d'écrire dans un fichier

def write_file(msg):
  file = open("jeu.txt", "w")
  file.write(msg)
  file.close()

#On créé la fonction pour lire dans le fichier

def read_file():
  file = open("jeu.txt", "r")
  msg = file.read()
  file.close()
  return msg

#Fonction enpêchant le Ctrl+C 

def stop_ctrlC(sig, frame):
    write_file('Pas ouf de CTRL+C ')
    exit()


signal.signal(signal.SIGINT, stop_ctrlC)


write_file("Démarrons un partie de plus ou moins ! Choississez un nombre entre 0 et 100")



#On initialise une boucle pour le plus ou moins

while end is False :
    #On va lire dans le file 
    saisi = read_file()
     #On vérifie la saisie utilisateur
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        if saisi > 100:
            continue          
        if saisi > solution :
            write_file('Trop grand !')       
        elif saisi < solution :
            write_file('Trop petit !')

        #Sinon on affiche le message de victoire et on arrete la boucle avec end=True 

        else :
            write_file('Gg a toi ! ')
            end = True
            fin()