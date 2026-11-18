from tkinter import *
from datetime import date

root = Tk()
root.title("dhfhhhd")
root.geometry("400x400")

lbl = Label(text="hey there", fg="white",bg="blue", height=1, width=300)
nameLbl = Label(text="enter full name", bg="yellow")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = "Welcome to the Application. \n Today's date is :"
    greet = "Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())

text_box = Text(height=3)
btn=Button(text="Click Me !", command=display, height=1, bg="blue", fg="white")

lbl.pack()
nameLbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()

  
    
