from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
# add widgets here
lbl=Label(window, text="cct", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
btn=Button(window, text="Không có gì để nhấn here", fg='green')
btn.place(x=0, y=100)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=100, y=250)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=20)
r2.place(x=180, y=20)
                
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=200, y=100)
C2.place(x=280, y=100)

window.title('Hello Python')
window.geometry("400x200+10+20")

window.mainloop()