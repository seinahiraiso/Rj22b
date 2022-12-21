import tkinter as tk
import os
from PIL import ImageTk
import time

root = tk.Tk()
root.geometry("400x400")
canvas = tk.Canvas(root, width=400,height=400,bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

dx=18
dy=3

id1=canvas.create_rectangle(17.5, 40, 72.5,60, fill="Blue",outline='Blue')
id2=canvas.create_rectangle(35, 27.5, 55,40, fill="Blue",outline='Blue')
id3=canvas.create_oval(20.5,60,40,75,fill="Black")
id4=canvas.create_oval(46,60,66,75,fill="Black")
x=50
y=50
Vx=5
X_current=300-dx

start=time.time()
stop_time=10

while True:
    canvas.coords(id1,x+17.5,y+40,x+dx+72.5,y+dy+60)
    canvas.coords(id2,x+35,y+27.5,x+dx+55,y+dy+40)
    canvas.coords(id3,x+18.5,y+60,x+dx+37,y+dy+70)
    canvas.coords(id4,x+55,y+60,x+dx+71,y+dy+70)
    
    x+=Vx
    if x<=0:
        Vx=abs(Vx)
    elif x>=X_current:
        Vx=-abs(Vx)
    time.sleep(0.02)
    root.update()

root.mainloop()
