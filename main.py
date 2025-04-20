from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Memorizer")

def open():
    #Open file using dialog
    fin = askopenfile(title="Open File")
    #If file name selected
    if fin is not None:
        #Delete item in listbox
        list.delete(0,END)
        #Read from file
        items = fin.readlines()
        #Insert to listbox
        for i in items:
            list.insert(END,i.strip())

def delete():
    index = list.curselection()
    if index:
        list.delete(index)

def save():
    #get file using dialog
    # default extension is optional, here will add .txt if missing
    fout = asksaveasfile(defaultextension=".txt")
    # if file name selected
    if fout is not None:
        for item in list.get(0,END):
            print(item.strip(),file=fout)

        list.delete(0,END)



def add():
    list.insert(END,txt.get())
    txt.delete(0,END)

open_btn = Button(window,text="Open",fg="blue",width=15,command=open)
open_btn.pack(side=LEFT,padx=10,pady=10)
delete_btn = Button(window,text="Delete",fg="red",width=15,command=delete)
delete_btn.pack(side=RIGHT,padx=10,pady=10)
save_btn = Button(window,text="Save",fg="green",width=15,command=save)
save_btn.pack(padx=10,pady=10)

txt = Entry(window,width=15)
txt.pack(padx=5,pady=5)

add_btn = Button(window,text="Add",fg="purple",width=15,command=add)
add_btn.pack(padx=10,pady=10)

frame = Frame(window)
scrollbar = Scrollbar(frame,orient="vertical")
list = Listbox(frame,width=30,bg="red",yscrollcommand=scrollbar)
list.pack(side=LEFT,padx=10,pady=10)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=list.yview)
frame.pack(side=LEFT)

window.mainloop()
