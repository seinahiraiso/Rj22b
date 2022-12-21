import tkinter as tk
import os
from PIL import ImageTk

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(17.5,40, 72.5,60, fill="Red",outline='Red')
canvas.create_rectangle(35, 27.5, 55,40, fill="Red",outline='Red')
canvas.create_oval(20.5,60,40,75,fill="Black")
canvas.create_oval(46,60,66,75,fill="Black")

canvas.create_rectangle(135, 150, 255,190, fill="Blue",outline='Blue')
canvas.create_rectangle(170, 125, 220,150, fill="Blue",outline='Blue')
canvas.create_oval(155,190,185,220,fill="Black")
canvas.create_oval(205,190,235,220,fill="Black")
			
root.mainloop()