import tkinter as tk

global cx
global cy

root = tk.Tk()
root.title("迷える工科トン")
root.geometry("1500x900")

canvas = tk.Canvas(root, background="#000", width=1500, height=900)
canvas.pack()

img = tk.PhotoImage(file="fig/0.png")
cx = 300
cy = 400

canvas.create_image(cx, cy, image=img tag="tori")

root.mainloop()
