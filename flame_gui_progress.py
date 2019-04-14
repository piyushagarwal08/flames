from tkinter import *
import flame_func as ff
import sys
def flames():  
    Boy = e1.get()
    Girl = e2.get()
    ff.Flames(Boy,Girl)
    
    
root = Tk()
root.geometry("700x300")
root.title("Flames the calculator")
root.resizable(True,True)


l1 = Label(root,text="Name of Boy: ",font = ("Arial",15),fg='red',bg='black')
l1.place(x=100,y=60)

l1 = Label(root,text="Name of Girl: ",font = ("Arial",15),fg="red",bg="black")
l1.place(x=100,y=90)

e1 = Entry(root,font =( "Arial",15),fg="blue")
e1.place(x=300,y=60)


e2 = Entry(root,font = ("Arial",15),fg="blue")
e2.place(x=300,y=90)

b1 = Button(root,text = "check your relation",command=lambda:flames(),font = ("Arial",15),fg="red")
b1.place(x=200,y=150)

l1 = Label(root,text="Flames the Calculator",font= ("Arial",15),fg='red',bg='black')
l1.place(x=200,y=10)


if(root.mainloop()):
    sys.exit()
