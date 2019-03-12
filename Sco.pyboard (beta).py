import math
import os
import tkinter
fin = 0
testeur = ""
    
def create_save():
    print("Création du fichier scoreboard")
    fichier = open("save.txt","w", encoding = "latin1")
    nom = input("choissisez un nom d'utilisateur : ")
    fichier.write("Partie de ")
    fichier.write(nom)
    fichier.write("\n")
    fichier.write("Co.py clicker, un projet par Lucas GROSJEAN (jeu) ; Otto HAJDU (Scoreboard et save) ; Ronan GUY (page web)")
    fichier.write("\n")
    fichier.write("\n")
    fichier.write("Points : 0")
    fichier.write("\n")
    fichier.write("Pen : default")
    fichier.write("\n")
    fichier.write("!testeur de debug de ficher save")
    fichier.close()


while fin == 0:
    if os.access("save.txt", os.F_OK) == True:
        print("fichier scoreboard détecté")
        print(" ")
        fichier = open("save.txt","r", encoding = "latin1")
        
        if Liste[:-1] == "testeur de debug de ficher save" :
            fichier.close()
            print(Texte)
            fin = fin + 1
        else:
            fichier.close()
            print("Le fichier save est incomplet ou corrumpu")
            print("Suppression du fichier....")
            os.remove("save.txt")
            create_save()
    else:
        create_save()


    
