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

root.mainloop()