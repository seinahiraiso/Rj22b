import tkinter as tk
import os
from PIL import ImageTk

root = tk.Tk()
root.geometry("1200x800")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

def blue(i,j):
	canvas.create_rectangle(17.5+(j*50+j+10), 40+(i*50+i+10), 72.5+(j*50+j+10),60+(i*50+i+10), fill="Blue",outline='Blue')
	canvas.create_rectangle(35+(j*50+j+10), 27.5+(i*50+i+10), 55+(j*50+j+10),40+(i*50+i+10), fill="Blue",outline='Blue')
	canvas.create_oval(20.5+(j*50+j+10),60+(i*50+i+10),40+(j*50+j+10),75+(i*50+i+10),fill="Black")
	canvas.create_oval(46+(j*50+j+10),60+(i*50+i+10),66+(j*50+j+10),75+(i*50+i+10),fill="Black")

	
def red(i,j):
	canvas.create_rectangle(17.5+(j*50+j+10), 40+(i*50+i+10), 72.5+(j*50+j+10),60+(i*50+i+10), fill="Red",outline='Red')
	canvas.create_rectangle(35+(j*50+j+10), 27.5+(i*50+i+10), 55+(j*50+j+10),40+(i*50+i+10), fill="Red",outline='Red')
	canvas.create_oval(20.5+(j*50+j+10),60+(i*50+i+10),40+(j*50+j+10),75+(i*50+i+10),fill="Black")
	canvas.create_oval(46+(j*50+j+10),60+(i*50+i+10),66+(j*50+j+10),75+(i*50+i+10),fill="Black")

for i in range(10):
	if (i % 2 == 0):
		for j in range(10):				
			if (j % 2 == 0):
				blue(i,j*1.2)
			else:
				red(i,j*1.2)
	else:
		for j in range(10):
			if (j%2 ==0):
				red(i,j*1.2)
			else:
				blue(i,j*1.2)
root.mainloop()
