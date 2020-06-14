import tkinter as tk #importing tkinter module with an abbreviation
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk() #creating main (root) catalogue of an application using class Tk()
root.title("Welcome to Tkinter!") #addind window title
but = tk.Button(root, text = "Congrats!")
but.place(x = 150, y = 150)


label = tk.Label(root, text="My first GUI App in Python!") # Create a text label
label.pack(padx=100, pady=100) # Pack it into the window


root.mainloop() #run the app (by entering the mainloop)

root.destroy()

