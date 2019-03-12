## Créateur de sauvegarde et Créateur de scoreboard de co.py clicker.
## Ne fonctionne que en local.
## Tâches restantes :
##  -Ranger le scoreboard (du plus grand ou plus petit nombre de points).
##  -Faire un scoreboard réseau.
##  -Importer le scoreboard sur Tkinter.

import os, sys, random
global name
global txtfilename
scorescore = []
scoreboard = []
temp = []
default_point_value = random.randint(0, 1000) #Temporaire pour tester le scoreboard, Sinon normalement 0
name = input("Quel est votre nom d'utilisateur ")
txtfilename = "sauvegarde/ "+ name + ".txt"

def savecreation(): #Créateur de sauvegarde
  print("Création de la sauvegarde")
  f=open(txtfilename,"w")
  f.write("Sauvegarde co.py clicker !\n\n")
  f.write("Utilisateur : ")
  f.write(name)
  f.write("\n")
  f.write("Points : ")
  f.write(str(default_point_value))
  f.close()
  print("Sauvegarde crée")

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
  liste = os.listdir("sauvegarde")
  for j in range(len(liste)):
    k = liste[j]
    nom = k.split(".")
    scoreboard.append(nom[0])
  for l in range(len(liste)):
    nomtxt = "sauvegarde/" +liste[l]
    euh = open(nomtxt, 'r')
    wuwu = euh.read()
    dada = wuwu.split("\n")
    del(dada[0:2])
    geg = " ".join(dada)
    tempo=geg.split("Utilisateur : ")
    del(tempo[0])
    tempa = "\n".join(tempo)
    temp = tempa.split(": ")
    scorescore.append(temp)
    euh.close()
  scoreprint = sorted(scorescore, key = lambda scorescore: scorescore[1], reverse=True)
  print(" ")
  print("Voici le Scoreboard!")
  print(" ")
  for z in range(len(scoreprint)):
    tempopa = ": ".join(scoreprint[z])
    print(tempopa)
    
  
    
elif scoretrue == "N":
  print("ok, fin du programme")
else:
  print(":(, fin du programme")



  
  
