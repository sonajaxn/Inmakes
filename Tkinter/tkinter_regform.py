from tkinter import *
root=Tk()

l1=Label(root,text="username")
l2=Label(root,text="Mob")
l3=Label(root,text="Email")
l4=Label(root,text="Age")
l5=Label(root,text="password")
l6=Label(root,text="Retype password")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)
entry6=Entry(root)

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
l3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
l4.grid(row=3,column=0)
entry4.grid(row=3,column=1)
l5.grid(row=4,column=0)
entry5.grid(row=4,column=1)
l6.grid(row=5,column=0)
entry6.grid(row=5,column=1)


b1=Button(root,text="LOGIN")
b2=Button(root,text="CANCEL")

b1.grid(row=6,column=0)
b2.grid(row=6,column=1)

root.mainloop()