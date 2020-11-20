from tkinter import * 
from tkinter.ttk import *
import os
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()

root.title("Elocutor Home")
root.iconbitmap(r"E:\Project\Elocutor\GUI Components Testing\images\icons8-siri-256.ico")
root.geometry("600x400")
uniform_color="#3b6dc7"


root.configure(background=uniform_color)

photo5 = PhotoImage(file = r"images/logo.png")
photoimage5 = photo5.subsample(0.8, 0.8)
l5=Label(root,image = photoimage5,background=uniform_color)
l5.pack()
l2 = Label(root, text = "Select Detection Method",background=uniform_color,foreground="white")
l2.config(font=('Arial Rounded MT Bold', 20))
l2.pack()
l3 = Label(root, text = "--------------------------------------------------------------------------------------------------------------------------------------------------\n",background=uniform_color,foreground="white")
l3.pack()
style = Style() 
style.configure('TButton', font = ('Arial', 15, 'bold'), borderwidth = '16', foreground ="black", background = uniform_color)

def button1_click():
    root.destroy


photo = PhotoImage(file = r"images/cheek.png") 
photoimage = photo.subsample(3, 3)
l4=Label(root,image = photoimage,background=uniform_color).place(x=30, y=250)
b1 = Button(root, text = 'Cheek', command = root.destroy, style="TButton").place(x=10, y=340)

photo1 = PhotoImage(file = r"images/eye3.png") 
photoimage1 = photo1.subsample(3, 3)
l5=Label(root,image = photoimage1,background=uniform_color).place(x=180, y=250)
b2 = Button(root, text = 'Eye').place(x=160, y=340)

photo2 = PhotoImage(file = r"images/eyebrows3.png") 
photoimage2 = photo2.subsample(3, 3)
l6=Label(root,image = photoimage2,background=uniform_color).place(x=330, y=250)
b3 = Button(root, text = 'Eyebrows').place(x=310, y=340)

photo3 = PhotoImage(file = r"images/exit3.png") 
photoimage3 = photo3.subsample(3, 3)
l7=Label(root,image = photoimage3,background=uniform_color).place(x=480, y=250)
b4 = Button(root, text = 'Exit',command=root.destroy).place(x=460, y=340)

root.mainloop()
