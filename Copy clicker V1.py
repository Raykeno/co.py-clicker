from tkinter import *
import tkinter as tk
import math
L=['morceau de charbon','Crayon de papier','Name3','Name4','Name5','Name6','Name7','Name8','Name9','Name10','Name11','Name12','Name13','Name14','Name15']
copiesC=0
A=100
AA=0
T=0







def clic_papier():
   global copiesC
   copiesC=copiesC+1+AA

   truc.config(text=copiesC, )

def am1():
    global copiesC,A,AA,T
    if copiesC>=A:
        AA+=1
        copiesC-=A
        A+=100
        T+=1
    if T==len(L):
        Bam1.config(text="ND",command="")
    else:
       truc.config(text=copiesC, )
       NomStylos.config(text=L[T])

















username=Tk()
Can2=Canvas(username,height=100,width=10,bg="blue")

fenetre=Tk()
fenetre.title("Co.py clicker")










Can=Canvas(fenetre,height=500,width=500,bg="grey")
Can.grid(row = 1 , column = 1)

Bcopies=Button(fenetre,text="click",command=clic_papier)
Bcopies.grid(row = 1 , column = 1)

Bam1=Button(fenetre,text="Name",command=am1)
Bam1.grid(row = 0 , column = 1)

truc=Label(fenetre, bg="lightblue", font="Arial 14")
truc.place(relx = 0.48, rely = 0.2)
truc.config(text=copiesC, )

NomStylos=Label(fenetre, bg="lightblue", font="Arial 14")
NomStylos.place(relx = 0.48, rely = 0.1)
NomStylos.config(text=L[0])



fenetre.mainloop()
username.mainloop()
