#First example
import tkinter as tk
o = tk.Tk()
g1 = tk.Button(o, text = "Button #1").place(x = 70, y = 50, height = 25, width = 80)
g2 = tk.Button(o, text = "Button #2").place(x = 70, y = 90, height = 25, width = 80)
g3 = tk.Button(o, text = "Button #3").place(x = 80, y = 130,height = 25, width = 60)
o.mainloop()

#2nd example
import tkinter as tk
o = tk.Tk()
g1 = tk.Button(o, text = "Button #1")
g2 = tk.Button(o, text = "Button #2")
g3 = tk.Button(o, text = "Button #3")
g1.pack()
g2.pack()
g3.pack()
o.mainloop()

#3rd example 
import tkinter as tk
o = tk.Tk()
g1 = tk.Button(o, text = "Button #1")
g2 = tk.Button(o, text = "Button #2")
g3 = tk.Button(o, text = "Button #3")
g1.pack(side = tk.LEFT)
g2.pack()
g3.pack()
o.mainloop()

#4th example
import tkinter as tk
o = tk.Tk()
g1 = tk.Button(o, text="Przycisk #1")
g2 = tk.Button(o, text="Przycisk #2")
g3 = tk.Button(o, text="Przycisk #3")
g1.grid(row=0,column=0)
g2.grid(row=1,column=1)
g3.grid(row=2,column=2)
o.mainloop()

#4th with columnspan
import tkinter as tk
o = tk.Tk()
g1 = tk.Button(o, text="Przycisk #1")
g2 = tk.Button(o, text="Przycisk #2")
g3 = tk.Button(o, text="Przycisk #3")
g1.grid(row=0,column=0)
g2.grid(row=1,column=1)
g3.grid(row=2,column=0,columnspan=2)
o.mainloop()

#5th example
import tkinter as tk
o = tk.Tk()
tk.Label(o, text = "Label:").pack()
tk.Button(o, text = "Button").pack()
switch = 0

tk.Checkbutton(o, text = "Switch", variable = switch).pack()
tk.Entry(o, width = 30).pack()
tk.Radiobutton(o, text = "Coffee", variable= switch, value = 1).pack()
tk.Radiobutton(o, text = "Tea", variable= switch, value = 2).pack()

o.mainloop()