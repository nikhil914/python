import tkinter
from tkinter import *
import sys


print("question 01")
root=Tk()
root.title("my app")
l1=Label(root,text="Hello World",fg='blue')
l1.place(x=70,y=50)
root.geometry("250x250")
root.maxsize(300,300)
root.minsize(200,200)
#root.resizable(False,False)
b=Button(root,text="exit",bg="red",fg="blue",width=25,command=exit)
b.place(x=50,y=100)
root.mainloop()




print("question 02")
root=Tk()
root.title("my app")
def show():
    l2 = Label(root, text="Hello world!", fg='red')
    l2.place(x=70,y=50)
l1=Label(root,text="Hello World!",fg='blue')
l1.place(x=70,y=50)
root.geometry("250x250")
root.maxsize(300,300)
root.minsize(200,200)
#root.resizable(False,False)
b=Button(root,text="show",bg="red",fg="blue",width=15,command=show)
b.place(x=50,y=100)
root.mainloop()





print("question 03")
root=Tk()
root.title("my app")
f1 = Frame(root)
def show():
    l2 = Label(f1, text="This is the new text", fg='red')
    l2.grid(row=3,column=1)

l1=Label(f1,text="Hello World!",fg='blue')
l1.grid(row=1, column=1)
root.geometry("250x250")
b=Button(f1,text="exit",bg="red",fg="blue",width=15,command=exit)
b.grid(row=0, column=0)
b=Button(f1,text="show",bg="red",fg="blue",width=15,command=show)
b.grid(row=2,column=0)
f1.pack()
root.mainloop()






print("question 05")
root=Tk()
root.title("my app")
def show():
    t1=entry.get()
    l2 = Label(root, text=t1, fg='red')
    l2.place(x=50,y=60)
entry=Entry(root,width='20')
entry.place(x=50,y=40)
root.geometry("250x250")
root.maxsize(300,300)
root.minsize(200,200)
root.resizable(False,False)
b=Button(root,text="exit",bg="red",fg="blue",width=15,command=exit)
b.place(x=50,y=150)
b=Button(root,text="show",bg="red",fg="blue",width=15,command=show)
b.place(x=50,y=100)
root.mainloop()




