## Créateur de sauvegarde et Créateur de scoreboard de co.py clicker.
## Ne fonctionne que en local.
## Tâches restantes :
##  -Ranger le scoreboard (du plus grand ou plus petit nombre de points).
##  -Faire un scoreboard réseau.
##  -Importer le scoreboard sur Tkinter.
from tkinter import *
import os, sys, random
global name
global txtfilename
scoreboard = []
temp = []
default_point_value = 0 #Temporaire pour tester le scoreboard, Sinon normalement 0
default_outil = "Morceau de charbon" #Outil par défaut
default_AM2 = "Vielle Imprimente" #Amelioration 2 par défaut
name = input("Quel est votre nom d'utilisateur ")
txtfilename = "sauvegarde/ "+ name + ".txt"


def savecreation(): #Créateur de sauvegarde
  print("Création de la sauvegarde")
  f=open(txtfilename,"w")
  f.write("Sauvegarde co.py clicker !\n\n")
  f.write(name)
  f.write("\n")
  f.write(str(default_point_value))
  f.write("\n")
  f.write(str(default_outil))
  f.write("\n")
  f.write(str(default_AM2))
  f.write("\n")
  f.close()
  print("Sauvegarde crée")

def scoreboardcreator():
  global scoreboardo
  liste = os.listdir("sauvegarde")
  scoreboardo = []
  for j in range(len(liste)):
    k = liste[j]
    nom = k.split(".")
    scoreboard.append(nom[0])
  for l in range(len(liste)):
    nomtxt = "sauvegarde/" +liste[l]
    euh = open(nomtxt, 'r')
    wuwu = euh.read()
    dada = wuwu.split("\n")
    del(dada[0:1], dada[-1])
    del(dada[0])
    scoreboardo += dada

  

  
if os.access(txtfilename , os.W_OK) == True :
  print("Sauvegarde détecté")
  print("Vérification")
  f=open(txtfilename, "r")
  verif = f.read(26) #Lis la 1ère ligne , "Sauvegarde co.py clicker !"
  f.close()
  if verif == "Sauvegarde co.py clicker !": # pour le futur lors d'un encryptage
    print("Sauvegarde vérifiée") #vérification meilleur avec tout le fichier mais cause beaucoup de problèmes
    print("Re-Bonjour, sur co.py clicker", name) 
  else:
    print("Sauvegarde non-reconnu")
    savecreation()
    print("Nous sommes désolés mais la sauvegarde a été refaite car elle est corrumpu :@")
    print("Re-Bonjour, sur co.py clicker", name)
    
else:
  print("Aucune sauvegarde")
  savecreation()
  print("Bienvenue, sur co.py clicker", name)

scoretrue = input("Voulez-vous voir le scoreboard?, N= non , Y=oui : ")
if scoretrue == "Y":
  scoreboardcreator()
    
  
    
elif scoretrue == "N":
  print("ok, fin du programme")
else:
  print(":(, fin du programme")


#Fenêtre scoreboard
Name=Tk()
Name.title("Scoreboard")
Name.resizable(width=False,height=True)
Name.geometry("350x950")
Name.config(bg="lightgrey")
label = Label(Name, text=scoreboardo, bg="lightgray")
label.pack()
bouton=Button(Name, text="Quitter le programme", command=Name.quit)
bouton.pack()
Name.mainloop()
  
  
