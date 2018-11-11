#! C:\Users\Valentin\AppData\Local\Programs\Python\Python36-32\python.exe
# 2b-auto
# jeu du plus ou moins dans un fichier
# 10/11/2018
# RAFFY Valentin

# on importe le module signal
import signal

# on import le module random
import random

# on import le module re
import re

# on importe le module time
import time

# on créé les variables nécessaires
solution = random.randint(0, 100)
end = False
count = 0
borneSup = 100
borneInf = 0
rep = 0


# on créé la fonction de fin


def fin():
    print("j'ai trouver "+str(rep)+" en "+str(count))
# on créé la fonction pour lire dans le fichier


def read_file():
    file = open("jeu.txt", "r")
    msg = file.read()
    file.close()
    return msg
# on créé la fonction pour écrire dans un fichier


def write_file(msg):
    file = open("jeu.txt", "w")
    file.write(msg)
    file.close()
# on initialise la boucle pour le jeu


while end is False:

    print("borne sup : " + str(borneSup) + " borne inf : " + str(borneInf))

    rep = round((borneSup + borneInf) / 2)
    write_file(str(rep))
    count += 1
    print(rep)
    time.sleep(2)
    data = read_file()
    print("data : " + data)

    if data == "Bien jouer":
        end = True
        print("gg")

    elif data == "Trop grand !":
        borneSup = rep
        print("trop grand")

    elif data == "Trop petit !":
        borneInf = rep
        print("trop petit")

fin()