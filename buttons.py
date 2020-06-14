'Buttons

import tkinter as tk

o = tk.Tk()
g1 = tk.Button(o, text = "Button #1").place(x = 70, y = 50, height = 25, width = 80)
g2 = tk.Button(o, text = "Button #2").place(x = 70, y = 90, height = 25, width = 80)
g3 = tk.Button(o, text = "Button #3").place(x = 80, y = 130,height = 25, width = 60)

o.mainloop()