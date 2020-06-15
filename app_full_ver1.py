import tkinter as tk
import webbrowser

def callback(url):
    webbrowser.open_new(url)

o = tk.Tk()
o.configure(background='#8E91BF')
o.geometry('500x570')
t1 = tk.Label(text = "Best search engine ever!", background='#8E91BF').place(x = 50, y = 20)
g1 = tk.Button(o, text="Google", command = lambda text="http://google.com": callback(text)).place(x = 400, y = 20, height = 30, width = 80)
t2 = tk.Label(text = "Stalk whomever you want", background='#8E91BF').place(x = 50, y = 70)
g2 = tk.Button(o, text="Facebook", command = lambda text="http://facebook.com": callback(text)).place(x = 400, y = 70, height = 30, width = 80)
t3 = tk.Label(text = "Check if your salary hasn''t arrived!", background='#8E91BF').place(x = 50, y = 120)
g3 = tk.Button(o, text="mBank", command = lambda text="http://mbank.pl": callback(text)).place(x = 400, y = 120, height = 30, width = 80)
t4 = tk.Label(text = "Broadcast yourself", background='#8E91BF').place(x = 50, y = 170)
g4 = tk.Button(o, text="YouTube", command = lambda text="http://youtube.com": callback(text)).place(x = 400, y = 170, height = 30, width = 80)
t5 = tk.Label(text = "Best music steaming provider born in Sweden", background='#8E91BF').place(x = 50, y = 220)
g5 = tk.Button(o, text="Spotify", command = lambda text="http://spotify.com": callback(text)).place(x = 400, y = 220, height = 30, width = 80)
t6 = tk.Label(text = "Willing to change the job?", background='#8E91BF').place(x = 50, y = 260)
g6 = tk.Button(o, text="LinkedIn", command = lambda text="http://linkedin.com": callback(text)).place(x = 400, y = 260, height = 30, width = 80)
t7 = tk.Label(text = "If you want to check your FB messages without scrolling...", background='#8E91BF').place(x = 50, y = 310)
g7 = tk.Button(o, text="Messenger", command = lambda text="http://messenger.com": callback(text)).place(x = 400, y = 310, height = 30, width = 80)
t8 = tk.Label(text = "Your mail service provided by Google", background='#8E91BF').place(x = 50, y = 360)
g8 = tk.Button(o, text="Gmail", command = lambda text="http://gmail.com": callback(text)).place(x = 400, y = 360, height = 30, width = 80)
t9 = tk.Label(text = "2nd biggest movie portal after IMDB", background='#8E91BF').place(x = 50, y = 410)
g9 = tk.Button(o, text="Filmweb", command = lambda text="http://filmweb.pl": callback(text)).place(x = 400, y = 410, height = 30, width = 80)
t10 = tk.Label(text = "Biggest movie streaming provider. Extremely politically correct", background='#8E91BF').place(x = 50, y = 460)
g10 = tk.Button(o, text="Netflix", command = lambda text="http://netflix.com": callback(text)).place(x = 400, y = 460, height = 30, width = 80)
t11 = tk.Label(text = "Willing to store your code?", background='#8E91BF').place(x = 50, y = 510)
g11 = tk.Button(o, text="Github", command = lambda text="http://github.com": callback(text)).place(x = 400, y = 510, height = 30, width = 80)
o.mainloop()

