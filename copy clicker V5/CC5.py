from tkinter import *
import tkinter as tk
import math,time,os,sys,pickle
from PIL import Image, ImageFont, ImageDraw, ImageTk








username = 0
L=['Morceau de charbon','Plume et encre','Pinceau à encre de chine noir','crayon de papier','Vieux Stylo','Stylo','Double Stylo','Stylo à plume','Stylo à plume de luxe','Stylo connecté', 'Stylo temporel','Stylo dimensionnel']
copiesC=0
click=0
achiv1get=0
autoC=0
prix1=0
prix2=0
AA=0
T=0






def savecreation(): #Créateur de sauvegarde
  print("Création de la sauvegarde")
  f=open(txtfilename,"wb")
  pickle.dump(copiesC,f)
  pickle.dump(click,f)
  pickle.dump(T,f)
  pickle.dump(autoC,f)
  pickle.dump(achiv1get,f)
  pickle.dump(prix1,f)
  pickle.dump(prix2,f)
  pickle.dump(AA,f)
  f.close()
  print("Sauvegarde crée")


def gestionsave():

    if os.access(txtfilename , os.W_OK) == True :
      global copiesC,click,achiv1get,autoC,prix1,prix2,AA,T
      print("Sauvegarde détecté")
      print("Re-Bonjour, sur co.py clicker", username)
      f=open(txtfilename,"rb")
      copiesC=pickle.load(f)
      click=pickle.load(f)
      T=pickle.load(f)
      autoC=pickle.load(f)
      achiv1get=pickle.load(f)
      prix1=pickle.load(f)
      prix2=pickle.load(f)
      AA=pickle.load(f)
      f.close()
      Prixam1.config(text=prix1)
      Prixam2.config(text=prix2)
      NomStylos.config(text=L[T])


    else:
      print("Aucune sauvegarde")
      savecreation()
      print("Bienvenue, sur co.py clicker", username)

def fermer():
    f=open(txtfilename,"wb")
    pickle.dump(copiesC,f)
    pickle.dump(click,f)
    pickle.dump(T,f)
    pickle.dump(autoC,f)
    pickle.dump(achiv1get,f)
    pickle.dump(prix1,f)
    pickle.dump(prix2,f)
    pickle.dump(AA,f)
    f.close()
    sys.exit()
















def validation():
    global username,txtfilename
    username = zone_de_saisi.get()
    if len(username)==0 :
        Name.title("veuillez rentrer un username:")

    else:
     global compteur,fenetre,Prixam1,Prixam2,NomStylos
     Name.destroy()
     txtfilename = "sauvegarde/ "+ username + ".txt"


     fenetre=Tk()
     fenetre.title("Co.py clicker")
     fenetre.resizable(width=False,height=False)
     fenetre.geometry("600x600")
     fenetre.config(bg="lightgrey")

     paper = Image.open("images/paper.png")
     tkpaper = ImageTk.PhotoImage(paper)
     Bcopies = Button(fenetre, text="click", command=clic_papier, image=tkpaper)
     Bcopies.place(relx=0.375, rely=0.32, height=216,width=150)

     Bam1=Button(fenetre,height=1,width=10,text="AM1",command=am1)
     Bam1.place(x=0,y=0)

     Bam2=Button(fenetre,height=1,width=10,text="AM2",command=am2)
     Bam2.place(x=80,y=0)


     Bscore= Button(fenetre, height=1, width=10, text="Scoreboard",command=fenscore)
     Bscore.place(x=520,y=0)

     BFermer=Button(fenetre,height=1,width=10,text="Fermer",command=fermer)
     BFermer.place(x=520,y=575)


     Prixam1=Label(fenetre, bg="lightblue", font="Arial 14")
     Prixam1.place(x=0,y=26)
     Prixam1.config(text=prix1)

     Prixam2=Label(fenetre, bg="lightblue", font="Arial 14")
     Prixam2.place(x=80,y=26)
     Prixam2.config(text=prix2)

     compteur=Label(fenetre, bg="lightblue", font="Arial 14")
     compteur.place(relx = 0.48, rely = 0.2)
     compteur.config(text=copiesC, )

     NomStylos=Label(fenetre, bg="lightblue", font="Arial 14")
     NomStylos.place(relx = 0.48, rely = 0.1,)
     NomStylos.config(text=L[0])

     Nom = Label(fenetre, bg="lightblue", font="Arial 14", text=username)
     Nom.place(relx = 0 , rely = 0.96)


     autoCor()
     gestionsave()
     fenetre.mainloop()





def fenscore():
    liste = os.listdir("sauvegarde")
    scoreboardname = ["Nom"]
    LCopieC=  ["CopieC"]
    LClick = ["Click"]
    Lam1 = ["AM1"]
    Lam2 = ["AM2"]
    for j in range(len(liste)):
      k = liste[j]
      nom = k.split(".")
      scoreboardname.append("\n")
      scoreboardname.append(nom[0],)
    for l in range(len(liste)):
      nomtxt = "sauvegarde/" +liste[l]
      f = open(nomtxt, 'rb')
      LCopieC+="\n"
      LCopieC+=str(pickle.load(f))
      LClick+="\n"
      LClick+=str(pickle.load(f),)
      Lam1+="\n"
      Lam1+=str(pickle.load(f),)
      Lam2+="\n"
      Lam2+=str(pickle.load(f),)




    score=Tk()
    score.title("Scoreboard")
    score.resizable(width=False,height=True)
    score.geometry("350x500")
    score.config(bg="lightgrey")
    label1 = Label(score, text=scoreboardname, bg="lightgray")
    label1.place(x=0, y=30)
    label2 = Label(score, text=LCopieC , bg="lightgray")
    label2.place(x=120,y=30)
    label3 = Label(score, text=LClick , bg="lightgray")
    label3.place(x=180,y=30)
    label4 = Label(score, text=Lam1 , bg="lightgray")
    label4.place(x=240,y=30)
    label5 = Label(score, text=Lam2 , bg="lightgray")
    label5.place(x=300,y=30)
    bouton=Button(score, text="Fermer", command=score.destroy)
    bouton.place(x=303,rely=0)
    score.mainloop()

























def clic_papier():
   global copiesC,click,achiv1get,autoC
   copiesC+=1+AA
   click+=1+AA
   compteur.config(text=copiesC)

   if click>=200 and achiv1get==0:
       autoC+=1
       achiv1get=1


def am1():
    global copiesC,prix1,AA,T
    if copiesC>=prix1:
        AA+=1
        copiesC-=prix1
        prix1+=100
        T+=1
        Prixam1.config(text=prix1)

    if T==len(L):
        Bam1.config(text="ND",command="")
    else:
       compteur.config(text=copiesC, )
       NomStylos.config(text=L[T])


def am2():
    global copiesC,prix2,autoC
    if copiesC>=prix2:
        autoC+=1
        copiesC-=prix2
        prix2+=100
        Prixam2.config(text=prix2)




def autoCor():
    global fenetre,copiesC,autoC,click
    copiesC += autoC
    click += autoC
    fenetre.after(1000, autoCor)
    compteur.config(text=copiesC)














Name=Tk()
dicimg = {}
Name.title("Votre username est :")
Name.resizable(width=False,height=False)
Name.geometry("387x247")
NameCan=Canvas(Name,width=387,height=247)
NameCan.place(x=0,y=0)

Logo = Image.open("images/Logo.png")
tkLogo = ImageTk.PhotoImage(Logo)
dicimg['img1'] = tkLogo
item = NameCan.create_image(193.5,123.5,image =tkLogo)
zone_de_saisi = Entry(Name)
zone_de_saisi.place(relx=0.35, rely =0.8 ,height=20)
Bvalid = Button(Name, text= 'Valider', command=validation)
Bvalid.place(relx=0.45, rely=0.9, height=20)



Name.mainloop()
