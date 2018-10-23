#! C:/Users/Valentin/AppData/Local/Programs/Python/Python36-32/python.exe
#1a-add
#Script permettant de faire des calculs
#Raffy Valentin
#15/10/2018

# On demande à l'utilisateur de choisir deux nombres à additionner
int1 = input("Entrez le premier nombre :")

while int1.isnumeric() != True:
  int1 = input ("Veuillez entrer un nombre :")


int2 = input ("Entrez le second nombre :")

while int2.isnumeric() != True:
  int2 = input ("Veuillez entrer un nombre :")

# Fonction qui additionne les deux nombres saisis
def addition(nb1, nb2):
      result = int(nb1) + int(nb2)
      print(result)

addition (int1, int2)

input("Appuyer sur une touche pour sortir")
