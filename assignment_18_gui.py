import tkinter
from tkinter import *
d={"rahul":88046378930,"mohit":7521654210,"malay":75421360245,"jyoti":45612335688,"radhika":78945612351,"nihal":789456123554}
root=Tk()
root.resizable(False,False)
root.geometry("70x70")
sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=sc.set)
for i in d:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)
Scrollbar(mylist,orient="vertical")
sc.config(command=mylist.yview)
root.mainloop()




d={"rahul":88046378930,"mohit":7521654210,"malay":75421360245,"jyoti":45612335688,"radhika":78945612351,"nihal":789456123554}
root=Tk()
root.resizable(False,False)
root.geometry("300x300")
sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=sc.set)
for i in d:
    mylist.insert(END,i)
entry=Entry(root,width=20)
entry.place(x=70,y=0)
entry1=Entry(root,width=20)
entry1.place(x=70,y=20)
mylist.place(x=20,y=90)
Scrollbar(mylist,orient="vertical")
sc.config(command=mylist.yview)
def show():
    k = entry.get()
    v = entry1.get()
    d[k]=v
    mylist.insert(END,k)
btn=Button(root,text="insert",command=show)
btn.place(x=90,y=50)
root.mainloop()






