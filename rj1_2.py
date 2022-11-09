import tkinter as tk
import os
from PIL import ImageTk

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(10, 140, 250,220, fill="Black")
canvas.create_rectangle(80, 90, 180,140, fill="Black")
canvas.create_oval(50,220,110,280,fill="Black")
canvas.create_oval(150,220,210,280,fill="Black")
canvas.create_text(70, 300, text="Seina Hiraiso", anchor=tk.NW, font=("",15))


root.mainloop()