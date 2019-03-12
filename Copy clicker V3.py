from tkinter import *
import tkinter as tk
import math
import time

username = 0
L=['morceau de charbon','Crayon de papier','Name3','Name4','Name5','Name6','Name7','Name8','Name9','Name10','Name11','Name12','Name13','Name14','Name15']
copiesC=0
click=0
achiv1get=0
autoC=0
prix1=0
prix2=0
AA=0
T=0

def validation():
    global username
    username = zone_de_saisi.get()
    if len(username)==0 :
        Name.title("veuillez rentrer un username:")

    else:
     Nom.config(text=username)
     Name.destroy()



def clic_papier():
   global copiesC,click,achiv1get,autoC
   copiesC+=1+AA
   click+=1+AA
   truc.config(text=copiesC, )

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


    if T==len(L):
        Bam1.config(text="ND",command="")
    else:
       truc.config(text=copiesC, )
       NomStylos.config(text=L[T])


def am2():
    global copiesC,prix2,autoC
    if copiesC>=prix2:
        autoC+=1
        copiesC-=prix2
        prix2+=100





def autoCor():
    global fenetre,copiesC,autoC,click
    copiesC += autoC
    click += autoC
    fenetre.after(1000, autoCor)
    truc.config(text=copiesC, )














Name=Tk()
Name.title("Votre username est :")
Name.resizable(width=False,height=False)

Can2=Frame(Name,height=100,width=300,bg="grey")
Can2.grid(row = 10 , column = 10)
zone_de_saisi = Entry(Name)
zone_de_saisi.grid(row=9,column=10)
Bvalid = Button(Name, text= 'Valider', command=validation)
Bvalid.grid(row=10,column=10)




fenetre=Tk()
fenetre.title("Co.py clicker")
fenetre.resizable(width=False,height=False)









Can=Frame(fenetre,height=600,width=600,bg="grey")
Can.grid(row = 10 , column = 10)

Bcopies=Button(fenetre,text="click",command=clic_papier)
Bcopies.grid(row = 10 , column = 10)

Bam1=Button(fenetre,text="Name ",command=am1)
Bam1.grid(row = 3 , column = 9)

Bam2=Button(fenetre,text="Name2",command=am2)
Bam2.grid(row = 1, column = 5)


truc=Label(fenetre, bg="lightblue", font="Arial 14")
truc.place(relx = 0.48, rely = 0.2)
truc.config(text=copiesC, )

NomStylos=Label(fenetre, bg="lightblue", font="Arial 14")
NomStylos.place(relx = 0.48, rely = 0.1)
NomStylos.config(text=L[0])

Nom = Label(fenetre, bg="lightblue", font="Arial 14")
Nom.place(relx = 0 , rely = 0.96)


autoCor()

fenetre.mainloop()
Name.mainloop()
